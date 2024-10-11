# ALGORITHM IMPLEMENTATION
def character_frequencies(text: str) -> dict:
    # create an array of character frequencies, where:
    # - the length of array (128) represents the number of ASCII code points
    # - the array indexes represent ASCII code points, where index `0` represents first ASCII code
    #   point `NUL` until index `127` which represents last ASCII code point `DEL`
    # - the array items represent character frequency for each ASCII code point
    frequencies = [0] * 128

    # calculate frequency for each character of `text`
    for char in text:
        # map each character of `text` to its ASCII code point
        code_point = ord(char)
        # increase the character frequency based on its ASCII code point
        frequencies[code_point] += 1

    # prepare results to be a python dictionary
    results = dict()
    i = 0
    while i < 128:
        # add non-zero frequencies to `results`
        if frequencies[i]:
            # - key: character as a string
            # - value: character frequency as an integer
            results[chr(i)] = frequencies[i]
        i += 1

    return results


# ALGORITHM USAGE
text = "Hello, World!"
text_frequency = character_frequencies(text)
for char, freq in text_frequency.items():
    print(f"`{char}` - {freq}")
"""Output would be:
` ` - 1
`!` - 1
`,` - 1
`H` - 1
`W` - 1
`d` - 1
`e` - 1
`l` - 3
`o` - 2
`r` - 1
"""

# ALGORITHM/CODE TIME COMPLEXITY ANALYSIS
"""
[CODE ANALYSIS]
def character_frequencies(text: str) -> dict:
    frequencies = [0] * 128                        f(n) = 1           = 1

    for char in text:                              f(n) = n           = n
        code_point = ord(char)                     f(n) = n           = n
        frequencies[code_point] += 1               f(n) = n           = n

    results = dict()                               f(n) = 1           = 1
    i = 0                                          f(n) = 1           = 1
    while i < 128:                                 f(n) = 128         = 128
        if frequencies[i]:                         f(n) = 128         = 128
            results[chr(i)] = frequencies[i]       f(n) = 128         = 128
        i += 1                                     f(n) = 128         = 128

    return results                                 f(n) = 1           = 1

[OVERALL RESULTS]
- Total f(n) = 3n + 516
- f(n) = O(n) as n -> infinity
- Time Complexity Class: Linear
"""
