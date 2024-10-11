# ALGORITHM IMPLEMENTATION
def std(x):
    # calculate items length
    x_len = len(x)

    # calculate mean value
    i= 0
    mean = 0
    while i < x_len:
        mean += x[i]
        i += 1
    mean /= x_len

    # calculate summation
    i= 0
    sum = 0
    while i < x_len:
        sum += (x[i] - mean)**2
        i += 1

    # calculate std
    std = (sum / x_len)**0.5

    return std


# ALGORITHM USAGE
print(std([5, 25, 75, 145, 555])) # 202.83983829612959