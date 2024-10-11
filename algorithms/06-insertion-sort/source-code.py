# ALGORITHM IMPLEMENTATION
def insertion_sort(n):
    i = 1
    while i < len(n):
        key = n[i]
        j = i-1
        while j >= 0:
            if n[j] > key:
                n[j+1] = n[j]
                j -= 1
            else:
                break
        n[j+1] = key
        i += 1
    return n


# ALGORITHM USAGE
print(insertion_sort([1, 500, 80, 8, 900, 1004, 0, 50, 93, 705, 4, 2])) # [0, 1, 2, 4, 8, 50, 80, 93, 500, 705, 900, 1004]


# ALGORITHM/CODE TIME COMPLEXITY ANALYSIS
"""
[CODE]
def insertion_sort(n):
    i = 1                        f(n) = 1           = 1
    while i < len(n):            f(n) = n           = n
        key = n[i]               f(n) = n           = n
        j = i-1                  f(n) = n           = n
        while j >= 0:            f(n) = n * n       = n^2
            if n[j] > key:       f(n) = n * n       = n^2
                n[j+1] = n[j]    f(n) = n * n       = n^2
                j -= 1           f(n) = n * n       = n^2
            else:
                break            f(n) = n * n       = n^2
        n[j+1] = key             f(n) = n           = n
        i += 1                   f(n) = n           = n
    return n                     f(n) = 1           = 1

[INFO]
- Total f(n) = 5n^2 + 5n + 2
- f(n) = O(n^2) as n -> infinity
- Time Complexity Class: Quadratic
"""