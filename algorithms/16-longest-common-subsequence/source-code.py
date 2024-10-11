# ALGORITHM IMPLEMENTATION
def build_lcs_table(text1, text2):
    # prepare the padding row and column to be added
    # to the table (their cell values would be zeros)
    text1 = " " + text1
    text2 = " " + text2

    n = len(text1)
    m = len(text2)

    # create the table
    table = [
        [None for _ in range(n)]
        for _ in range(m)
    ]

    # fill the table
    for i in range(m):
        for j in range(n):
            # add padding cells
            if i == 0 or j == 0:
                table[i][j] = 0
            # if there is a matching, cell value = 1 + top_left_corner_cell
            elif text2[i] == text1[j]:
                table[i][j] = 1 + table[i-1][j-1]
            # if there is NOT a matching, cell value = max(top_cell, left_cell)
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return table

def find_lcs(text1, text2):
    table = build_lcs_table(text1, text2)

    # start from the bottom right cell
    i = len(text2)
    j = len(text1)

    lcs = ""
    while i > 0 and j > 0:
        if table[i][j] > table[i][j-1]:
            if table[i][j] == table[i-1][j]:
                # the current cell value inherited from the top cell
                i -= 1 # move to top row
            else:
                # the current cell value is the origin of match
                lcs = text2[i-1] + lcs # add char to solution
                i -= 1 # move to top row
                j -= 1 # move to left column
        else:
            j -= 1 # move to left column

    return lcs


# ALGORITHM USAGE (I)
print(find_lcs("HELLOWORLD", "OHELOD")) # HELOD


# ALGORITHM USAGE (II)
print(find_lcs("XMJYAUZ", "MZJAWXU")) # MJAU
