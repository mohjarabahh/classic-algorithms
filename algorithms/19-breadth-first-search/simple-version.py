# ALGORITHM IMPLEMENTATION
from queue import Queue

def breadth_first_search(graph: dict) -> list:
    # create queue of vertices
    queue = Queue()
    # create hash-table of visited vertices
    visited = {}

    # determine first vertex
    first = next(iter(graph.items()))[0]

    # select first vertex
    # - enqueue first vertex
    queue.put(first)
    # - mark first vertex as visited
    visited[first] = True

    solution = []
    while not queue.empty():
        # dequeue current vertex
        current = queue.get()
        # retrieve array of destination vertices for current vertex
        destinations = graph[current]

        for dest in destinations:
            if not visited.get(dest):
                # select destination vertex
                # - enqueue destination vertex
                queue.put(dest)
                # - mark destination vertex as visited
                visited[dest] = True

                # add current edge to solution
                solution.append(f"{current}-{dest}")

    return solution


# ALGORITHM USAGE
edges = breadth_first_search(
    graph = {
        "A": ["B", "C"],
        "B": ["E", "D", "A"],
        "C": ["D", "F", "A"],
        "D": ["E", "F", "B"],
        "E": ["F", "B"],
        "F": ["D", "E", "C", "H"],
        "G": ["H", "I"],
        "H": ["G", "I", "F"],
        "I": ["G", "H"]
    }
)

for edge in edges:
    print(edge)

"""Output would be:
A-B
A-C
B-E
B-D
C-F
F-H
H-G
H-I
"""
