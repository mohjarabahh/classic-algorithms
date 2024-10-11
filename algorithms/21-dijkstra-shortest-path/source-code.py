# ALGORITHM IMPLEMENTATION
from sys import float_info
MAX = float_info.max # largest floating-point number

class Vertex:
    def __init__(self):
        self.label                 : str          = ""
        self.links                 : list['Edge'] = []
        self.total_length          : float        = 0.0
        self.source_of_total_length: Vertex       = None

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

    def add_edges(self, source: int, targets: list[int], weights: list[float]):
        # retrieve source vertex from array of vertices (based on array index)
        source_vertex = self.vertices[source]

        for target, weight in zip(targets, weights):
            # retrieve target vertex from array of vertices (based on array index)
            target_vertex = self.vertices[target]

            # add new link to links of source vertex
            # i.e. link source vertex with target vertex via new edge WITH A SPECIFIC WEIGHT!
            source_vertex.links.append(Edge(source_vertex, target_vertex, weight))

    def greedy_dijkstra(self) -> tuple[float, str]:
        # retrieve first vertex
        first = self.vertices[0]

        # initialize total length of all vertices
        for vertex in self.vertices:
            if vertex is first:
                vertex.total_length = 0
            else:
                vertex.total_length = MAX

        # apply greedy strategy to calculate total length
        for vertex in self.vertices:
            # retrieve array of destination vertices
            destinations = vertex.links

            # if current vertex does not have any destination vertices, continue
            if destinations == []:
                continue
            # otherwise, apply greedy strategy
            else:
                for edge in destinations:
                    # - retrieve destination vertex
                    dest = edge.target

                    # - calculate total length for destination vertex
                    # where, total length(dest) = total length(current) + edge weight
                    new_length = vertex.total_length + edge.weight

                    # - choose only minimum total length
                    if new_length < dest.total_length:
                        dest.total_length = new_length
                        dest.source_of_total_length = vertex

        # store minimum length
        minimum_length = self.vertices[-1].total_length

        # track labels of shortest path
        # - retrieve last vertex
        vertex = self.vertices[-1]
        # - start path with last vertex
        path = vertex.label
        # - track path labels
        while vertex.source_of_total_length is not None:
            path = vertex.source_of_total_length.label + "-" + path
            vertex = vertex.source_of_total_length

        #  reset all vertices for future processing/operations
        self.reset_vertices()

        return minimum_length, path

    def reset_vertices(self):
        """
        - reset `total_length` to `0.0` for all vertices
        - reset `source_of_total_length` to `None` for all vertices
        """

        for vertex in self.vertices:
            vertex.total_length = 0.0
            vertex.source_of_total_length = None


# ALGORITHM USAGE
graph = Graph(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

graph.add_edges(0, [1, 2, 3], [2, 4, 3])
graph.add_edges(1, [4, 5, 6], [7, 4, 6])
graph.add_edges(2, [4, 5, 6], [3, 2, 4])
graph.add_edges(3, [4, 5, 6], [4, 1, 5])
graph.add_edges(4, [7, 8], [1, 4])
graph.add_edges(5, [7, 8], [6, 3])
graph.add_edges(6, [7, 8], [3, 3])
graph.add_edges(7, [9], [3])
graph.add_edges(8, [9], [4])

length, path = graph.greedy_dijkstra()
print(length) # 11
print(path) # A-C-E-H-J
