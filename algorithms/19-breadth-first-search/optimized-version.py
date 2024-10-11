# ALGORITHM IMPLEMENTATION
from queue import Queue

class Vertex:
    def __init__(self):
        self.label   : str          = ""
        self.visited : bool         = False
        self.links   : list['Edge'] = []

class Edge:
    def __init__(self, source: Vertex, target: Vertex, weight: float = 0.0):
        self.source = source
        self.target = target
        self.weight = weight

class Graph:
    def __init__(self, labels: list[str]):
        # create array of vertices
        l = len(labels)
        self.vertices = [Vertex() for _ in range(l)]

        # assign labels to all vertices
        for vertex, label in zip(self.vertices, labels):
            vertex.label = label

    def add_edges(self, source: int, targets: list[int]):
        # retrieve source vertex from array of vertices (based on array index)
        source_vertex = self.vertices[source]

        for target in targets:
            # retrieve target vertex from array of vertices (based on array index)
            target_vertex = self.vertices[target]

            # add new link to links of source vertex (i.e. link source vertex with target vertex via new edge)
            source_vertex.links.append(Edge(source_vertex, target_vertex))

    def breadth_first_search(self) -> list[str]:
        # create queue of vertices
        queue = Queue()

        # retrieve first vertex
        first = self.vertices[0]

        # select first vertex
        # - enqueue first vertex
        queue.put(first)
        # - mark first vertex as visited
        first.visited = True

        solution = []
        while not queue.empty():
            # dequeue current vertex
            current = queue.get()
            # retrieve array of destination vertices for current vertex
            destinations = current.links

            for edge in destinations:
                dest = edge.target
                if not dest.visited:
                    # select destination vertex
                    # - enqueue destination vertex
                    queue.put(dest)
                    # - mark destination vertex as visited
                    dest.visited = True

                    # add current edge to solution
                    solution.append(f"{current.label}-{dest.label}")

        # reset visited flag/mark to `False` for all vertices
        self.reset_vertices()

        return solution

    def reset_vertices(self):
        for vertex in self.vertices:
            vertex.visited = False


# ALGORITHM USAGE
graph = Graph(["A", "B", "C", "D", "E", "F", "G", "H", "I"])

graph.add_edges(0, [1, 2])
graph.add_edges(1, [0, 3, 4])
graph.add_edges(2, [0, 3, 5])
graph.add_edges(3, [1, 2, 4])
graph.add_edges(4, [1, 5])
graph.add_edges(5, [2, 3, 4, 7])
graph.add_edges(6, [7, 8])
graph.add_edges(7, [5, 6, 8])
graph.add_edges(8, [6, 7])

edges = graph.breadth_first_search()
for edge in edges:
    print(edge)

"""Output would be:
A-B
A-C
B-D
B-E
C-F
F-H
H-G
H-I
"""
