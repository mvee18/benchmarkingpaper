import numpy as np
import pandas as pd

from scipy.stats.mstats import gmean
from scipy.spatial.distance import euclidean
from scipy.stats import mannwhitneyu


def clr(x):
    """Centered log ratio transform"""
    return np.log(x / gmean(x))


def aitchison(x: np.array, y: np.array) -> float:
    """Aitchison distance"""
    return euclidean(clr(x), clr(y))


def replace_zeroes(a: np.array, v: float = 0.001) -> np.array:
    """Replace zeroes with a small value. For use with CLR transform."""
    return np.where(a == 0, v, a)


def replace_zero_aitchison(x: np.array, y: np.array) -> float:
    """Aitchison distance with zeroes replaced by a small value"""
    return aitchison(replace_zeroes(x), replace_zeroes(y))


def mann_whitney(x: np.array, y: np.array) -> float:
    """Mann-Whitney U test"""
    return mannwhitneyu(x, y)[1]
