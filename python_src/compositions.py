import numpy as np
import pandas as pd

from scipy.stats.mstats import gmean
from scipy.spatial.distance import euclidean
from scipy.stats import mannwhitneyu

from skbio.stats.composition import multiplicative_replacement


def clr(x):
    """Centered log ratio transform"""
    return np.log(x / gmean(x))


def aitchison(x: np.array, y: np.array) -> float:
    """Aitchison distance"""
    return euclidean(clr(x), clr(y))


def const_replace_zeroes(a: np.array, v: float = 0.001) -> np.array:
    """Replace zeroes with a small value. For use with CLR transform."""
    return np.where(a == 0, v, a)


def const_replace_zero_aitchison(x: np.array, y: np.array) -> float:
    """Aitchison distance with ONLY zeroes replaced by a small value"""
    return aitchison(const_replace_zeroes(x), const_replace_zeroes(y))


def add_constant(a: np.array, v: float = 0.001) -> np.array:
    """Add a constant to an array"""
    return a + v


def add_constant_aitchison(x: np.array, y: np.array, v: float = 0.001) -> float:
    """Aitchison distance with a constant added to EACH value"""
    return aitchison(add_constant(x, v), add_constant(y, v))


def multiplicative_aitchison(x: np.array, y: np.array, delta: float) -> float:
    """Aitchison distance with multiplicative replacement"""
    return aitchison(multiplicative_replacement(x, delta=delta), multiplicative_replacement(y, delta=delta))


def uniform_replace_zeroes(a: np.array, dl: float) -> np.array:
    """
    Parameters:
    -----------
    a: np.array
        Array to replace zeroes in
    dl: float
        Upper bound (should be minimum value in arrays.)

    Returns:
    --------
    np.array
        Array with zeroes replaced by uniform distribution
    """
    # The DL is already 0.10 * dl, so we need to multiply by 10.
    unif_val = np.random.uniform(dl, 10*dl)
    # print("replacing with uniform draw: ", unif_val)
    return np.where(a == 0, unif_val, a)


def mann_whitney(x: np.array, y: np.array) -> float:
    """Mann-Whitney U test"""
    return mannwhitneyu(x, y)[1]
