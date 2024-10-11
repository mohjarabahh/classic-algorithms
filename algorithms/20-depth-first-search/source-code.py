# ALGORITHM IMPLEMENTATION
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
    solution = []

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

    def __dfs_recursion(self, current: Vertex):
        # mark current vertex as visited
        current.visited = True

        # retrieve array of destination vertices for current vertex
        destinations = current.links

        for edge in destinations:
            dest = edge.target
            if not dest.visited:
                # mark destination vertex as visited
                dest.visited = True

                # add current edge to solution
                self.solution.append(f"{current.label}-{dest.label}")

                # visit destination vertex
                self.__dfs_recursion(dest)

    def depth_first_search(self) -> list[str]:
        # retrieve first vertex
        first = self.vertices[0]

        # visit first vertex
        self.__dfs_recursion(first)

        # reset visited flag/mark to `False` for all vertices
        self.reset_vertices()

        return self.solution

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

edges = graph.depth_first_search()
for edge in edges:
    print(edge)

"""Output would be:
A-B
B-D
D-C
C-F
F-E
F-H
H-G
G-I
"""
