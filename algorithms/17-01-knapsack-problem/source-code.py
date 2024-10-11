# ALGORITHM IMPLEMENTATION
class Item:
    def __init__(self, name, weight, profit):
        self.name: str = name
        self.weight: int = weight
        self.profit: int = profit

def knapsack_select(items, max_weight):
    # add empty item to ease the procedures later
    items.insert(0, Item("#0", 0, 0))

    # determine rows and columns of the table
    rows = len(items)
    cols = max_weight+1

    # create the table
    table = [
        [None for _ in range(cols)]
        for _ in range(rows)
    ]

    # fill the table
    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif items[i].weight <= j:
                table[i][j] = max(
                    table[i-1][j],
                    items[i].profit + table[i-1][j - items[i].weight]
                )
            else:
                table[i][j] = table[i-1][j]

    # determine the max profit
    max_profit = table[i][j]

    # select the items that can be carried in knapsack
    knapsack = []
    remain = max_weight
    while remain >= 0 and j > 0:
        if table[i][j] > table[i-1][j]:
            knapsack.append(items[i].name)
            remain -= items[i].weight
            j = remain
        i -= 1

    return knapsack, max_profit


# ALGORITHM USAGE
knapsack, max_profit = knapsack_select(
    items = [
        Item("#1", 1, 4),
        Item("#2", 3, 9),
        Item("#3", 5, 12),
        Item("#4", 4, 11)
    ],
    max_weight = 8
)
print(knapsack) # ["#4", "#2", "#1"]
print(max_profit) # 24
