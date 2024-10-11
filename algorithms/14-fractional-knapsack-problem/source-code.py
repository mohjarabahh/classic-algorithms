# ALGORITHM IMPLEMENTATION
def greedy_knapsack_select(
    items:        tuple[tuple[int, int], ...],
    max_capacity: int | float
    ) ->          tuple[tuple[int, int], ...]:

    # calculate ratio of profit-per-1kg of the items
    new = []
    for profit, weight in items:
        new.append((profit, weight, profit/weight))

    # sort items descending by ratio (i.e. item at index `2` in `new`)
    new.sort(key = lambda a: a[2], reverse = True)

    # select the maximum items that can be carried in knapsack to achieve the maximum profit
    knapsack = []
    capacity = 0

    for profit, weight, ratio in new:
        # - calculate available space in knapsack
        available = max_capacity - capacity

        # - if item weight is less than available space, add the item
        if capacity < max_capacity and weight < available:
            knapsack.append((profit, weight))
            capacity += weight

        # - otherwise, add fraction of item, then stop
        else:
            knapsack.append((ratio * available, available))
            capacity += available
            break

    return tuple(knapsack)


# ALGORITHM USAGE
items = ((4, 1), (9, 2), (12, 10), (11, 4), (6, 3), (5, 5))
max_capacity = 12
print(greedy_knapsack_select(items, max_capacity)) # ((9, 2), (4, 1), (11, 4), (6, 3), (2.4, 2))


# ALGORITHM/CODE TIME COMPLEXITY ANALYSIS
"""
[CODE ANALYSIS]
def greedy_knapsack_select(items, max_capacity):
    new = []                                                               f(n) = 1
    for profit, weight in items:                                           f(n) = n
        new.append((profit, weight, profit/weight))                        f(n) = n

    new.sort(key = lambda a: a[2], reverse = True)                         f(n) = n log n

    knapsack = []                                                          f(n) = 1
    capacity = 0                                                           f(n) = 1

    for profit, weight, ratio in new:                                      f(n) = n
        available = max_capacity - capacity                                f(n) = n

        if capacity < max_capacity and weight < available:                 f(n) = n
            knapsack.append((profit, weight))                              f(n) = n
            capacity += weight                                             f(n) = n

        else:
            knapsack.append((ratio * available, available))                f(n) = n
            capacity += available                                          f(n) = n
            break

    return tuple(knapsack)                                                 f(n) = 1


[OVERALL RESULTS]
- f(n) = n log n + 9n + 4
- f(n) = O(n log n) as n -> infinity
"""