"""
Arithmetic Coding
"""
class ArithmeticCoding:
    """Arithmetic Coding implementation.

    This class implements arithmetic coding for encoding and decoding data
    based on provided probabilities.

    Methods:
        encode(symbol_list, probabilities, data) -> float:
            Encodes the given data using arithmetic coding based on provided
            probabilities.

        find_symbol_for_value(probabilities, value) -> Any:
            Given a value, finds the symbol that it represents using the
            cumulative probabilities.

        decode(symbol_list, probabilities, encoded_value, data_length) -> list:
            Decodes the encoded value using the provided probabilities and
            returns the original data.
    """
    symbol_list = []
    probabilities = {}

    @staticmethod
    def encode(arr):
        """Encode the data using arithmetic coding based on provided probabilities.

        Args:
            symbol_list (list): The list of symbols in the data.
            probabilities (dict): A dictionary mapping symbols to their
                cumulative probability ranges.
            data (list): The data to be encoded.

        Returns:
            float: The encoded value.
        """
        low = 0.0
        high = 1.0
        for symbol in arr:
            range_ = high - low
            high = low + range_ * ArithmeticCoding.probabilities[symbol][1]
            low = low + range_ * ArithmeticCoding.probabilities[symbol][0]
        return (low + high) / 2

    @staticmethod
    def find_symbol_for_value(value):
        """Given a value, find the symbol that it represents using the cumulative probabilities.

        Args:
            probabilities (dict): A dictionary mapping symbols to their
                cumulative probability ranges.
            value (float): The value to find the symbol for.

        Returns:
            Any: The symbol that the value represents, or None if the value
                is not within any symbol's probability range.
        """
        for symbol, (low, high) in ArithmeticCoding.probabilities.items():
            if low <= value < high:
                return symbol
        return None

    @staticmethod
    def decode(encoded_bits, meta):
        """Decode the data using the provided encoded value and probabilities.

        Args:
            symbol_list (list): The list of symbols in the data.
            probabilities (dict): A dictionary mapping symbols to their
                cumulative probability ranges.
            encoded_bits (float): The encoded value to be decoded.
            meta : data_length (int): The length of the original data.

        Returns:
            list: The decoded output data.
        """
        current_value = encoded_bits
        decoded_output = []
        for _ in range(meta):
            symbol = ArithmeticCoding.find_symbol_for_value(current_value)
            decoded_output.append(symbol)
            range_ = ArithmeticCoding.probabilities[symbol][1] - ArithmeticCoding.probabilities[symbol][0]
            current_value = (current_value - ArithmeticCoding.probabilities[symbol][0]) / range_
        return decoded_output

if __name__ == '__main__':
    ArithmeticCoding.symbols = [0.1 * k for k in range(11)]
    ArithmeticCoding.probabilities = {0: (0.0, 0.7), 1: (0.7, 0.85), 0.1: (0.85, 1.0)}
    data = [0, 0, 0.1, 0.1, 0, 0, 0, 1, 0, 0, 1, 0.1, 0, 0]
    encoded_value = ArithmeticCoding.encode(data)
    decoded_output = ArithmeticCoding.decode(encoded_value, len(data))
    print(f"Encoded Value: {encoded_value}")
    print(f"Decoded Output: {decoded_output}")
