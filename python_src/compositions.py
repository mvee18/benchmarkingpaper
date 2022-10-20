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


def mann_whitney(x: np.array, y: np.array) -> float:
    """Mann-Whitney U test"""
    return mannwhitneyu(x, y)[1]
