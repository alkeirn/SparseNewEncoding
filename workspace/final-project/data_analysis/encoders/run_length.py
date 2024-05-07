"""
_summary_
"""
from encoder import Encoder
import numpy as np

class RunLength(Encoder):
    """
    an encoder which stores length of repetitions
    """
    def encode(self, arr):
        """
        Encode a numpy array using run-length encoding.
        """
        edges = np.diff(arr) != 0
        changes = np.where(edges)[0] + 1
        indices = np.r_[0, changes]  # Include the start index

        # Compute run lengths and the corresponding values
        run_lengths = np.diff(np.r_[indices, arr.size])
        values = arr[indices]
        run_lengths.dtype = np.uint8

        return values, run_lengths

    def decode(self, encoded_bits, meta):
        """
        Decode a run-length encoded sequence.
        Args:
            encoded_bits: unique values encoded
            meta: lengths of repetition
        """
        return np.repeat(encoded_bits, meta)
