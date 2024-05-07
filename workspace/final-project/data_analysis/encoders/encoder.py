"""
This is a basic module for abstract encoder
"""
from typing import Tuple
import numpy as np

class Encoder:
    """
    Abstract class for encoder
    """
    @staticmethod
    def encode(arr:np.ndarray)->Tuple(str, object):
        """
        This function encodes the given array

        Args:
            arr (np.ndarray): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
    @staticmethod
    def decode(encoded_bits:str, meta:object)->np.ndarray:
        """
        _summary_

        Args:
            encoded_bits (str): _description_
            meta (object): _description_

        Raises:
            NotImplementedError: _description_

        Returns:
            np.ndarray: _description_
        """
        raise NotImplementedError
