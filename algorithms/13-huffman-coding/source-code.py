# ALGORITHM IMPLEMENTATION
from heapq import heappush as enqueue
from heapq import heappop  as dequeue

class HeapNode:
    def __init__(self, character: str, frequency: int) -> None:
        """Initializes a heap node with a character (`str`) and its frequency (`int`)."""

        self.character: str = character
        self.frequency: int = frequency
        self.left     : HeapNode | None = None
        self.right    : HeapNode | None = None

    def __lt__(self, other: "HeapNode") -> bool:
        """
        Compares two heap nodes based on their frequency. This allow `frequency (int)` attribute
        to be used in the `priority queue` algorithm (i.e. `heap queue`) as the priority of the node to maintaining the queue invariant.

        #### More Details:
        The less-than operator (`__lt__` magic method) is used in the `heapq` module, specifically in the `_siftdown` and `_siftup` functions
        to compare two `HeapNode` objects based on their specific attribute which is defined with the `__lt__` magic method (`frequency` attribute in this case).
        """

        return self.frequency < other.frequency

class GreedyHuffmanCoding:
    null_char = chr(0)
    huffman_codes = dict()

    def __init__(self, text: str) -> None:
        """
        Initialize the HuffmanCoding object.

        This method performs the following steps:
        1. Calculates the frequency of each character in the given text.
        2. Converts the frequency dictionary into a priority queue (heap queue).
        3. Builds the Huffman coding tree based on the character frequencies.
        4. Assigns binary codes to characters using the Huffman tree.
        """

        # calculate frequencies of characters of `text`
        frequencies = self._calculate_frequencies(text)

        # convert `frequencies` from dictionary (i.e. Hash Table) to priority queue (i.e. heap queue)
        frequencies = self._convert_frequencies(frequencies)

        # build huffman coding tree
        huffman_tree = self._build_tree(frequencies)

        # assign codes to characters
        root_node: HeapNode = huffman_tree[0]
        self._assign_codes(root_node, root_node.character)

    def _calculate_frequencies(self, text: str) -> dict:
        """Calculates frequencies of characters of `text (str)`."""

        # create dictionary of character frequencies
        frequencies = dict()

        # calculate frequency for each character of `text`
        for char in text:
            if frequencies.get(char):
                frequencies[char] += 1
            else:
                frequencies[char] = 1

        return frequencies

    def _convert_frequencies(self, frequencies: dict) -> list:
        """Converts `frequencies (dict)` from dictionary (i.e. Hash Table) to priority queue (a.k.a. heap queue)."""

        min_heap = []
        for char, freq in frequencies.items():
            enqueue(min_heap, HeapNode(char, freq))

        return min_heap

    def _build_tree(self, heap_queue: list) -> list:
        """Builds huffman coding tree."""

        # loop until single node remains in heap queue (i.e. root node only)
        while len(heap_queue) != 1:
            # extract two nodes with minimum frequency
            left = dequeue(heap_queue)
            right = dequeue(heap_queue)

            # create a new internal node, where:
            # - node frequency equals to the sum of frequencies of extracted nodes
            # - node character is NULL (`NUL`), because it's an internal node and doesn't represent a specific character
            internal_node = HeapNode(self.null_char, left.frequency + right.frequency)

            # assign extracted nodes as children to internal node
            internal_node.left = left
            internal_node.right = right

            # add new internal node back to heap queue
            enqueue(heap_queue, internal_node)

        return heap_queue

    def _assign_codes(self, node: HeapNode, code: str) -> None:
        """Assigns huffman codes to characters."""

        # base case: `HeapNode` object or `None`?
        if node == None:
            return 0

        # assign codes to characters
        if node.character != self.null_char:
            self.huffman_codes[node.character] = code

        # recursive case
        self._assign_codes(node.left,  code + "0")
        self._assign_codes(node.right, code + "1")

    def get_codes(self) -> dict:
        """Returns huffman codes of character of input text."""

        return self.huffman_codes


# ALGORITHM USAGE
compressed_text = GreedyHuffmanCoding("Huffman Coding is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters.")
text_codes = compressed_text.get_codes()
for char, code in text_codes.items():
    print(f"`{char}` - {code}")

"""Output would be:
`e` - 000
`s` - 001
`r` - 0100
`t` - 0101
`i` - 0110
`n` - 0111
`v` - 1000000
`b` - 1000001
`u` - 100001
`p` - 100010
`m` - 100011
`o` - 1001
` ` - 101
`g` - 11000
`H` - 11001000
`-` - 11001001
`,` - 11001010
`q` - 11001011
`C` - 11001100
`T` - 11001101
`.` - 1100111
`h` - 11010
`d` - 11011
`a` - 1110
`c` - 11110
`f` - 111110
`l` - 111111
"""