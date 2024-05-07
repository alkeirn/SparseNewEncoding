"""Delta Value Encoding.

This class implements the Delta Value Encoding algorithm for encoding and
decoding NumPy arrays. The Delta Value Encoding algorithm encodes an array
by representing each value as the difference from the previous value.

Attributes:
    None

Methods:
    encode(arr: np.ndarray) -> np.ndarray:
        Encodes the input array using the Delta Value Encoding algorithm.

    decode(encoded_bits: np.ndarray, meta=None) -> np.ndarray:
        Decodes an encoded array back to its original form.
"""
from encoder import Encoder
import numpy as np

class Delta(Encoder):
    """ Delta Value Encoding """
    @staticmethod
    def encode(arr: np.ndarray) -> np.ndarray:
        """Encodes the input array using the Delta Value Encoding algorithm.

        Args:
            arr (np.ndarray): The input array to be encoded.

        Returns:
            np.ndarray: The encoded array.
        """
        return np.diff(arr)
    @staticmethod
    def decode(encoded_bits: np.ndarray, meta=None) -> np.ndarray:
        """Decodes an encoded array back to its original form.

        Args:
            encoded_bits (np.ndarray): The encoded array.
            meta (None, optional): Not used in this implementation.

        Returns:
            np.ndarray: The decoded array.
        """
        # Initialize the decoded array with the first value of the original array
        decoded_arr = [encoded_bits[0]]

        # Reconstruct the original array by accumulating the differences
        for diff in encoded_bits[1:]:
            decoded_arr.append(decoded_arr[-1] + diff)

        return np.array(decoded_arr)
