# ALGORITHM IMPLEMENTATION
class SortedCharacterFrequencies:
    def ascii_characters(self, text: str) -> dict:
        # create array of character frequencies, where:
        # - length of array (128) represents number of ASCII code points
        # - array indexes represent ASCII code points (e.g. `65`, `97`, `48`)
        # - array items represent character frequency for each ASCII code point
        frequencies = [0] * 128

        # calculate frequency for each character of `text`
        for char in text:
            # map each character of `text` to its ASCII code point
            code_point = ord(char)
            # increase the character frequency based on its ASCII code point
            frequencies[code_point] += 1

        # create dictionary to store `sorted character frequencies`
        sor_char_freq = dict()
        i = 0
        while i < 128:
            # add non-zero frequencies to `sor_char_freq`
            if frequencies[i]:
                # - key: character as a string
                # - value: character frequency as an integer
                sor_char_freq[chr(i)] = frequencies[i]
            i += 1

        return sor_char_freq

    def utf8_characters(self, text: str) -> dict:
        # create dictionary of character frequencies, where:
        # - dictionary keys represent characters of UTF-8 code points (e.g. `A`, `a`, `🤓`)
        # - dictionary values represent character frequencies
        frequencies = dict()

        # calculate frequency for each character of `text`
        for char in text:
            # increase the character frequency
            # - if character already exist, increase its frequency
            if frequencies.get(char):
                frequencies[char] += 1
            # - otherwise, assign value of `1`` as character frequency
            else:
                frequencies[char] = 1

        return frequencies

    def sort_frequencies(self, frequencies: dict) -> dict:
        # convert `frequencies` from dictionary to 2-dimensional array
        array = []
        for char, freq in frequencies.items():
            array.append( [char, freq] )

        # sort `array` ascending by the value of character frequency (the second item in nested arrays with index `1`)
        # time complexity of `list.sort()` method is O(n log n)
        array.sort(key = lambda a: a[1])

        # convert `array` from 2-dimensional array to dictionary
        frequencies = dict()
        for char, freq in array:
            frequencies[char] = freq

        return frequencies


# ALGORITHM USAGE
text = "Hello, World!"
instance = SortedCharacterFrequencies()

frequencies = instance.utf8_characters(text)
for c, f in frequencies.items():
    print(f"`{c}` - {f}")
"""Output would be:
`H` - 1
`e` - 1
`l` - 3
`o` - 2
`,` - 1
` ` - 1
`W` - 1
`r` - 1
`d` - 1
`!` - 1
"""

print("*"*15)

frequencies = instance.sort_frequencies(frequencies)
for c, f in frequencies.items():
    print(f"`{c}` - {f}")
"""Output would be:
`H` - 1
`e` - 1
`,` - 1
` ` - 1
`W` - 1
`r` - 1
`d` - 1
`!` - 1
`o` - 2
`l` - 3
"""

# ALGORITHM/CODE TIME COMPLEXITY ANALYSIS
"""
[ascii_characters]
- Total f(n) = 3n + 516
- f(n) = O(n) as n -> infinity
- Time Complexity Class: Linear

[utf8_characters]
- Total f(n) = 4n + 2
- f(n) = O(n) as n -> infinity
- Time Complexity Class: Linear

[sort_frequencies]
- Total f(n) = n*log(n) + 4n + 3
- f(n) = O(n log n) as n -> infinity
"""
