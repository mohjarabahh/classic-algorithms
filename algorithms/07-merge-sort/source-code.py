# ALGORITHM IMPLEMENTATION
def merge_sort(n, start, end):
    # base case
    if start >= end:
        return 0
    # recursive case
    else:
        mid = (start + end)//2
        merge_sort(n, start, mid)
        merge_sort(n, mid+1, end)
        merge(n, start, mid, end)

def merge(n, start, mid, end):
    # divide the array into two halves
    left_side = n[start : mid+1]
    right_side = n[mid+1 : end+1]

    # sort the elements of the two halves, and merge them to the main array
    l = r = 0
    i = start
    while (l < len(left_side)) and (r < len(right_side)):
        if left_side[l] < right_side[r]:
            n[i] = left_side[l]
            l += 1
            i += 1
        else:
            n[i] = right_side[r]
            r += 1
            i += 1

    # merge the remaining elements of either half to the main array
    while l < len(left_side):
        n[i] = left_side[l]
        l += 1
        i += 1
    while r < len(right_side):
        n[i] = right_side[r]
        r += 1
        i += 1


# ALGORITHM USAGE
array = [50, 1, 30, 77, 66, 0, 8, 1, 101]
merge_sort(array, 0, len(array)-1)
print(array) # [0, 1, 1, 8, 30, 50, 66, 77, 101]


# ALGORITHM/CODE TIME COMPLEXITY ANALYSIS
"""
Using the recursion tree method, the f(n) = n * (k + 1), where:
- `n` is the number of inputs
- `k` is the number of last level of recursion tree, where recursion tree start from `level 0`

Also, experimentally, it has been shown that:
- when n = 4,  then k = 2
- when n = 8,  then k = 3
- when n = 16, then k = 4
- so, k = log2(n)

Finally, we got that:
- f(n) = n * (log2(n) + 1) = n * log2(n) + n
- f(n) = O(n log n) as n -> infinity
"""