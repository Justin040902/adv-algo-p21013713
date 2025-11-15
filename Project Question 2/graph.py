from typing import TypeVar, Generic, List, Dict, Optional

T = TypeVar('T')


class Graph(Generic[T]):
    def __init__(self):
        self.vertices: List[T] = []
        self.adjacency_list: Dict[T, List[T]] = {}
        self.incoming_edges: Dict[T, List[T]] = {}  # For tracking followers

    def add_vertex(self, vertex: T) -> None:
        """Add a new vertex to the graph"""
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.adjacency_list[vertex] = []
            self.incoming_edges[vertex] = []

    def add_edge(self, from_vertex: T, to_vertex: T) -> None:
        """Connect one vertex with another vertex (directed edge)"""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)

        if to_vertex not in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].append(to_vertex)

        if from_vertex not in self.incoming_edges[to_vertex]:
            self.incoming_edges[to_vertex].append(from_vertex)

    def remove_edge(self, from_vertex: T, to_vertex: T) -> None:
        """Remove an edge between two vertices"""
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].remove(to_vertex)

        if to_vertex in self.incoming_edges and from_vertex in self.incoming_edges[to_vertex]:
            self.incoming_edges[to_vertex].remove(from_vertex)

    def list_outgoing_adjacent_vertex(self, vertex: T) -> List[T]:
        """List all vertices in which edges are outgoing from this vertex"""
        return self.adjacency_list.get(vertex, [])

    def list_incoming_adjacent_vertex(self, vertex: T) -> List[T]:
        """List all vertices that have edges pointing to this vertex (followers)"""
        return self.incoming_edges.get(vertex, [])

    def get_all_vertices(self) -> List[T]:
        """Get all vertices in the graph"""
        return self.vertices.copy()

    def vertex_exists(self, vertex: T) -> bool:
        """Check if a vertex exists in the graph"""
        return vertex in self.vertices



