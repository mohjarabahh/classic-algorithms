# ALGORITHM IMPLEMENTATION
def binary_search(array, key):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (high + low)//2
        if key == array[mid]:
            return mid
        elif key > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ALGORITHM USAGE
n = [11, 42, 59, 73, 101, 125, 159, 183, 204, 228, 245, 268, 302] # the array must be a sorted array
print(binary_search(n, 159)) # 6
print(binary_search(n, 155)) # -1


# ALGORITHM/CODE TIME COMPLEXITY ANALYSIS
"""
- f(n) = O(log n) as n -> infinity
- Time Complexity Class: Logarithmic
"""