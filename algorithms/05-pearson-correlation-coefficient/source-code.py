# ALGORITHM IMPLEMENTATION
def correlation(x, y):
    # calculate values length
    n = len(x)

    # calculate x_sum, y_sum, x2_sum, y2_sum, xy_sum
    i = x_sum = y_sum = x2_sum = y2_sum = xy_sum = 0
    while i<n:
        x_sum += x[i]
        y_sum += y[i]
        x2_sum += x[i]**2
        y2_sum += y[i]**2
        xy_sum += x[i] * y[i]
        i += 1

    # calculate compound formulas x_sqrt and y_sqrt
    x_sqrt = (n * x2_sum - (x_sum)**2)**0.5
    y_sqrt = (n * y2_sum - (y_sum)**2)**0.5

    # calculate R
    r = (n * xy_sum - x_sum * y_sum) / (x_sqrt * y_sqrt)

    return r


# ALGORITHM USAGE
print(correlation([288, 333, 884, 105, 66], [470, 606, 88.70, 175, 78.80])) #-0.11559223566136385