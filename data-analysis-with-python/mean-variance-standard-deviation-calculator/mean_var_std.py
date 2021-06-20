from typing import List
import numpy as np


def calculate(list: List[int]):
    """
    Compute the mean, variance, standard deviation, max, min,
    and sum of the rows, columns, and elements in a 3 x 3 matrix.

    Parameters:
        - list: an array of exactly 9 integers
    """
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    data = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [data.mean(axis=0).tolist(), data.mean(axis=1).tolist(), data.mean()],
        'variance': [data.var(axis=0).tolist(), data.var(axis=1).tolist(), data.var()],
        'standard deviation': [data.std(axis=0).tolist(), data.std(axis=1).tolist(), data.std()],
        'max': [data.max(axis=0).tolist(), data.max(axis=1).tolist(), data.max()],
        'min': [data.min(axis=0).tolist(), data.min(axis=1).tolist(), data.min()],
        'sum': [data.sum(axis=0).tolist(), data.sum(axis=1).tolist(), data.sum()]
    }

    return calculations
