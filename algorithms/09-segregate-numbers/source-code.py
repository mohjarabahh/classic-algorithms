# PROBLEM STATEMENT
"""
[PROBLEM TITLE]
Segregate Positive and Negative Numbers

[PROBLEM DESCRIPTION]
Given an array of integers containing both positive and negative numbers. The task is to segregate the positive and negative numbers in
the array without sorting them explicitly. The "Merge Sort" technique must used to rearrange the elements such that all negative numbers
appear before the positive numbers while maintaining the relative order of negative and positive numbers within their respective groups.

[EXAMPLE]
- Input : [9, -3, 5, -2, -8, -6, 1, 3]
- Output: [-3, -2, -8, -6, 9, 5, 1, 3]
"""


# ALGORITHM IMPLEMENTATION
def merge_segregate(n, start, end):
    # base case
    if start >= end:
        return 0
    # recursive case
    else:
        mid = (start + end)//2
        merge_segregate(n, start, mid)
        merge_segregate(n, mid+1, end)
        merge(n, start, mid, end)
def merge(n, start, mid, end):
    # divide the array into two halves
    left_side = n[start : mid+1]
    right_side = n[mid+1 : end+1]

    # segregate the elements of the two halves, and merge them to main array
    l = r = 0
    i = start
    while (l < len(left_side)) and (r < len(right_side)):
        # does the element of left halve is a negative number?, then merge it to main array
        if left_side[l] < 0:
            n[i] = left_side[l]
            l += 1
            i += 1
        # does the element of right halve is a negative number?, then merge it to main array
        elif right_side[r] < 0:
            n[i] = right_side[r]
            r += 1
            i += 1
        # once no halves have negative number, then stop the segregation
        else:
            break

    # merge the remaining elements of either half to the main array. start merging from left halve to right halve!
    # left halve
    while l < len(left_side):
        n[i] = left_side[l]
        l += 1
        i += 1
    # right halve
    while r < len(right_side):
        n[i] = right_side[r]
        r += 1
        i += 1


# ALGORITHM USAGE
array = [9, -3, 5, -2, -8, -6, 1, 3]
merge_segregate(array, 0, len(array)-1)
print(array) # [-3, -2, -8, -6, 9, 5, 1, 3]


# ALGORITHM/CODE TIME COMPLEXITY ANALYSIS
"""
f(n) = O(n log n) as n -> infinity
"""