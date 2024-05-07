"""
_summary_

Returns:
    _type_: _description_
"""
import sys
from matplotlib import pyplot as plt
import numpy as np
from torchvision import transforms
import torch


def get_dataset(tv_class, data_path ='./data', train=True, download=True, batch=100, shuffle=False):
    """
    This returns dataset and dataloader for a given class of dataset from torchvision
     tv_class : a class imported from torchvision.datasets
    """
    transform = transforms.Compose([
            transforms.ToTensor(),
        ])
    data_set = tv_class(root=data_path, train=train, download=download, transform=transform)
    return data_set, torch.utils.data.DataLoader(data_set, batch_size=batch, shuffle=shuffle)


def plot_histogram(data, title, num_bins=256, normalize=False, hist_color='blue'):
    """
    Utility function for plotting histogram.
    Args:
        data: np.ndarray flattened
        title: string; plot title
        num_bins: int; number of histogram bins; default: 256
        normalize: bool; if true shows frequency density instead of actual frequency; default: False
        hist_color: string; color filled in bins; default: blue
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=num_bins, color=hist_color, edgecolor='black', density=normalize)
    plt.title(title)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency Density' if normalize else 'Frequency')
    plt.grid(True)
    plt.show()

def delta_sparcity(pixels):
    """
    _summary_

    Args:
        pixels (_type_): _description_

    Returns:
        _type_: _description_
    """
    delta_values = np.diff(pixels)
    sparcity = {
        'zero_sparcity_before': 1 - np.count_nonzero(pixels)/len(pixels),
        'zero_sparcity_after': 1 - np.count_nonzero(delta_values)/len(delta_values)
    }
    return delta_values, sparcity



def generate_sparse_array(sparse_fraction, unique_fraction, size):
    """
    _summary_

    Args:
        sparse_fraction (_type_): _description_
        unique_fraction (_type_): _description_
        size (_type_): _description_

    Returns:
        _type_: _description_
    """
    arr = np.zeros(size)
    random_size = int((1 - sparse_fraction) * size)
    unique_size = unique_fraction # int(unique_fraction * random_size)

    if unique_size > 0:
        unique_values = np.random.randn(unique_size)
        full_values = np.tile(unique_values, (random_size // unique_size + 1))[:random_size]
        np.random.shuffle(full_values)
        arr[:random_size] = full_values

    np.random.shuffle(arr)
    return arr

def size_compare(data, compressor, encoder, decoder):
    """
    _summary_

    Args:
        data (_type_): _description_
        compressor (_type_): _description_
        encoder (_type_): _description_
        decoder (_type_): _description_

    Returns:
        _type_: _description_
    """
    return {
        'orginal_size': sys.getsizeof(data),
        'encoded_size': sys.getsizeof(encoder(data)[0]) + sys.getsizeof(encoder(data)[1]),
        'encoded_compressed_size': sys.getsizeof(encoder(compressor(data))[0]) + sys.getsizeof(encoder(compressor(data))[1])
    }


def total_variation_distance(p, q):
    """
    Calculate the total variation distance between two discrete probability mass functions.
    p and q are lists representing the PMFs.
    """
    if len(p) != len(q):
        raise ValueError("The two lists must have the same length.") 
    tv_dist = 0.5 * sum(abs(p_i - q_i) for p_i, q_i in zip(p, q))
    return tv_dist



def load_pretrained_model(model_class):
    """
    _summary_

    Args:
        model_class (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = model_class(pretrained = True)
    weights = {}

    # Traverse all model parameters and tensors
    for name, param in model.named_parameters():
        weights[name] = param.data  # .data gives the tensor

    return weights
