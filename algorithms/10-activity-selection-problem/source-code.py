# ALGORITHM I/O ANALYSIS & PSEUDOCODE
"""
[I/O ANALYSIS]
- Input(s)  : start, end
- Process(s): starting with the first activity, then select the next activity that starts after the current activity finishes
- Output(s) : results

[PSEUDOCODE]
- DECLARE VARIABLES: start, end, results = []
- DECLARE VARIABLES: s, e = 1, 0
- INPUT start, end
- results = [0]
- LOOP FROM (s) TO (start.length-1) WHERE (s+=1) AFTER EACH ITERATION END
---- IF (start[s] >= end[e]), THEN
------- results.append(s)
------- e = s
- OUTPUT results
"""


# ALGORITHM IMPLEMENTATION
def greedy_activity_select(start, end):
    # starting with the first activity
    results = [0]

    # select the next activity that starts after the current activity finishes
    s, e = 1, 0
    while s <= len(start)-1:
        if start[s] >= end[e]:
            results.append(s)
            e = s
        s += 1
    return results


# ALGORITHM USAGE
start_time = [ 9, 10, 11, 12, 13, 15]
end_time   = [11, 11, 12, 14, 15, 16]
print(greedy_activity_select(start_time, end_time))  # [0, 2, 3, 5]


# ALGORITHM/CODE TIME COMPLEXITY ANALYSIS
"""
[CODE ANALYSIS]
def activity_select(start, end):
    results = [0]                        f(n) = 1           = 1
    s, e = 1, 0                          f(n) = 1           = 1
    while s <= len(start)-1:             f(n) = n           = n
        if start[s] >= end[e]:           f(n) = n           = n
            results.append(s)            f(n) = n           = n
            e = s                        f(n) = n           = n
        s += 1                           f(n) = n           = n
    return results                       f(n) = 1           = 1

[OVERALL RESULTS]
- Total f(n) = 5n + 3
- f(n) = O(n) as n -> infinity
- Time Complexity Class: Linear
"""