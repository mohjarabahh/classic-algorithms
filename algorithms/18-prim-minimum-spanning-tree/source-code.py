# ALGORITHM IMPLEMENTATION
from sys import float_info

def greedy_prim_mst(graph, labels):
    # prepare some data
    # - largest floating-point number
    MAX = float_info.max
    # - number of vertices
    vertices = len(labels)
    # - number of selected edges
    edges = 0
    # - array of selected vertices
    solution = [False for _ in range(vertices)]

    # select the first vertex
    solution[0] = True

    while edges < vertices-1:
        # temporal variables
        # - store the minimum weight, initialized first time with `MAX`
        min_ = MAX
        # - store the position of minimum weight, initialized first time with `-1` for both `from_` and `to_`
        from_, to_ = -1, -1

        for i in range(vertices):
            if solution[i] == True:
                for j in range(vertices):
                    if (solution[j] == False) and (min_ > graph[i][j] > 0):
                        # update temporal variables
                        min_ = graph[i][j]
                        from_, to_ = i, j

        # select the current vertex and increase the counter of selected edges
        solution[to_] = True
        edges += 1

        # in each step, print the results
        print(f"{labels[from_]}-{labels[to_]}: {graph[from_][to_]}")


# ALGORITHM USAGE
greedy_prim_mst(
    graph=[
        [0, 6.7, 5.2, 2.8, 5.6, 3.6],
        [6.7, 0, 5.7, 7.3, 5.1, 3.2],
        [5.2, 5.7, 0, 3.4, 8.5, 4.0],
        [2.8, 7.3, 3.4, 0, 8.0, 4.4],
        [5.6, 5.1, 8.5, 8.0, 0, 5.6],
        [3.6, 3.2, 4.0, 4.4, 4.6, 0]
    ],
    labels=["1", "2", "3", "4", "5", "6"]
)

""" Output would be:
1-4: 2.8
4-3: 3.4
1-6: 3.6
6-2: 3.2
6-5: 4.6
"""
