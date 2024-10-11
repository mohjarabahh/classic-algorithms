# ALGORITHM IMPLEMENTATION
from sys import maxsize as MAX

class Node:
    label: str = "" # label of the node
    total: int = 0  # total cost of the node
    to   : str = "" # label of the next node

class StagecoachRoute:
    def __init__(self, costs, labels):
        self.nodes = self.calculate_cost(costs, labels)
        self.path = self.find_path(self.nodes, labels)

    def calculate_cost(self, costs, labels):
        """Calculates the total cost of the cheapest path."""

        n = len(costs)
        nodes = [Node() for _ in range(n)]

        # outer loop: backward from `n-2` to `0`
        for i in range(n-2, -1, -1):
            currentNode = nodes[i]
            currentNode.label = labels[i]
            currentNode.total = MAX

            # inner loop: forward from `i+1` to `n-1`
            for j in range(i + 1, n):
                nextNode = nodes[j]

                # cost to next node (from adjacency matrix)
                costToNext = costs[i][j]

                # process only non-zero cost values
                if costToNext:
                    # total cost of current node = cost to next node + total cost of next node
                    currentTotal = costToNext + nextNode.total

                    # store the minimum total cost with label of next node
                    if currentTotal < currentNode.total:
                        currentNode.total = currentTotal
                        currentNode.to = labels[j]

        return nodes

    def find_path(self, nodes, labels):
        """Concatenates the nodes of the cheapest path."""

        path = []

        # add first node
        path.append(labels[0])

        # concatenate minimum cost path
        next = nodes[0].to
        for node in nodes:
            if node.label == next:
                path.append(next)
                next = node.to

        # add last node
        path.append(labels[-1])

        return "-".join(path)

    def get_cost(self):
        """Returns the total cost of the cheapest path as an integer."""

        return self.nodes[0].total

    def get_path(self):
        """Returns the nodes of the cheapest path as a string."""

        return self.path


# ALGORITHM USAGE (I)
route = StagecoachRoute(
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    costs = [
        [0, 2, 4, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 4, 6, 0, 0, 0],
        [0, 0, 0, 0, 3, 2, 4, 0, 0, 0],
        [0, 0, 0, 0, 4, 1, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
)
print(route.get_cost()) # 11
print(route.get_path()) # A-C-E-H-J


# ALGORITHM USAGE (II)
route = StagecoachRoute(
    labels = ["A", "B", "C", "D", "E", "F", "G"],
    costs = [
        [0, 9, 8, 0, 0, 0, 0],
        [0, 0, 0, 7, 6, 5, 0],
        [0, 0, 0, 4, 3, 2, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0]
    ]
)
print(route.get_cost()) # 13
print(route.get_path()) # A-C-D-G
