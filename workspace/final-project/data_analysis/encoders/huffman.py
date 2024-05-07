"""
_summary_
"""
import heapq
from collections import Counter
import numpy as np
from encoder import Encoder

class Node:
    """
    _summary_
    """
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(value_freq):
    """Build the Huffman Tree based on valueacter frequencies."""
    priority_queue = [Node(value, freq) for value, freq in value_freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]  # Return the root node of the Huffman tree

def generate_codes(node, prefix="", code_map=None):
    """Generate Huffman codes for valueacters."""
    if code_map is None:
        code_map = {}

    if node.value is not None:
        code_map[node.value] = prefix
    else:
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)

    return code_map

class Huffman(Encoder):
    """
    _summary_
    """
    @staticmethod
    def encode(arr:np.ndarray):
        # Encode a numpy array using Huffman coding.
        freq = Counter(arr.flat)            # Calculate frequency of each symbol
        root = build_huffman_tree(freq)
        codes = generate_codes(root)
        encoded_output = ''.join(codes[val] for val in arr.flat)
        return encoded_output, codes, root
    @staticmethod
    def decode(encoded_bits:str, meta:Node):
        """
        _summary_

        Args:
            encoded_bits (_type_): _description_
            root (_type_): _description_

        Returns:
            _type_: _description_
        """
        decoded_output = []
        current = meta
        for bit in encoded_bits:
            if bit == '0':
                current = current.left
            else:
                current = current.right

            if current.value is not None:
                decoded_output.append(current.value)
                current = meta

        return np.array(decoded_output)
