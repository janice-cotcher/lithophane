import numpy as np
from collections import defaultdict

def coords_to_indices(vertices: np.ndarray, vectors: np.ndarray) -> np.ndarray:
    """
    Convert a [F, 3, 3] array of triangle vertex coordinates
    into a [F, 3] integer index array referencing rows in vertices.
    
    vertices: [V, 3] unique vertex coordinates
    vectors:  [F, 3, 3] triangle vertex coordinates
    """
    # Build a lookup: coord tuple -> index in vertices
    lookup = {tuple(v): i for i, v in enumerate(vertices)}
    
    F = vectors.shape[0]
    triangles = np.zeros((F, 3), dtype=np.int64)
    
    for fi in range(F):
        for corner in range(3):
            coord = tuple(vectors[fi, corner])
            triangles[fi, corner] = lookup[coord]
    
    return triangles

def compute_normals(vertices: np.ndarray, triangles: np.ndarray) -> np.ndarray:
    """[F, 3] unit normals for each face."""
    coords = vertices[triangles]
    v0 = coords[:, 1, :] - coords[:, 0, :]
    v1 = coords[:, 2, :] - coords[:, 0, :]
    normals = np.cross(v0, v1)
    norms = np.linalg.norm(normals, axis=1, keepdims=True)
    return normals / np.where(norms == 0, 1, norms)


def build_edge_to_faces(triangles: np.ndarray) -> dict:
    """
    Map each edge (frozenset of 2 vertex indices) -> list of face indices.
    An edge shared by exactly 2 faces is a manifold edge.
    """
    edge_to_faces = defaultdict(list)
    for fi, tri in enumerate(triangles):
        for i in range(3):
            edge = frozenset([tri[i], tri[(i + 1) % 3]])
            edge_to_faces[edge].append(fi)
    return edge_to_faces


def find_crease_edges(vertices: np.ndarray, triangles: np.ndarray,
                      target_angle_deg: float = 90.0,
                      tolerance_deg: float = 10.0) -> list[tuple]:
    """
    Find all edges where the two adjacent faces meet at approximately
    target_angle_deg (within +/- tolerance_deg).

    Returns a list of (vi, vj, angle_deg) tuples for qualifying edges.
    """
    normals = compute_normals(vertices, triangles)
    edge_to_faces = build_edge_to_faces(triangles)

    crease_edges = []
    lo = np.radians(target_angle_deg - tolerance_deg)
    hi = np.radians(target_angle_deg + tolerance_deg)

    for edge, faces in edge_to_faces.items():
        if len(faces) != 2:
            continue  # skip boundary or non-manifold edges

        fi, fj = faces
        dot = np.dot(normals[fi], normals[fj])
        angle = np.arccos(np.clip(dot, -1.0, 1.0))

        if lo <= angle <= hi:
            vi, vj = tuple(edge)
            crease_edges.append((vi, vj, np.degrees(angle)))

    return crease_edges


def chain_crease_edges(crease_edges: list[tuple]) -> list[list[int]]:
    """
    Chain qualifying edges into continuous vertex paths by following
    shared endpoints. Each path is a list of vertex indices in order.

    Forks (a vertex shared by 3+ crease edges) are handled by
    greedily picking the first unvisited branch — you can replace
    this with angle-based continuation if needed.
    """
    # Build adjacency from crease edges only
    adj = defaultdict(set)
    for vi, vj, _ in crease_edges:
        adj[vi].add(vj)
        adj[vj].add(vi)

    visited_edges = set()
    paths = []

    def trace_path(start: int) -> list[int]:
        """Follow a chain from start until it dead-ends or loops."""
        path = [start]
        prev = None
        current = start

        while True:
            neighbours = adj[current] - ({prev} if prev else set())
            unvisited = [
                n for n in neighbours
                if frozenset([current, n]) not in visited_edges
            ]
            if not unvisited:
                break

            next_v = unvisited[0]
            visited_edges.add(frozenset([current, next_v]))
            path.append(next_v)
            prev = current
            current = next_v

        return path

    # Start chains from endpoints (degree 1) first for cleaner paths,
    # then handle loops or interior-only networks
    endpoints = [v for v, neighbours in adj.items() if len(neighbours) == 1]
    start_candidates = endpoints if endpoints else list(adj.keys())

    for start in start_candidates:
        # Check if this vertex still has unvisited edges
        has_unvisited = any(
            frozenset([start, n]) not in visited_edges
            for n in adj[start]
        )
        if has_unvisited:
            paths.append(trace_path(start))

    return paths