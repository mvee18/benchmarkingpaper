from compositions import clr
from compositions import aitchison
from compositions import replace_zeroes
from compositions import replace_zero_aitchison
import numpy as np


def test_clr():
    test_np = np.array([0.1, 0.3, 0.4, 0.2])
    assert np.allclose(clr(test_np), np.array(
        [-0.79451346,  0.30409883,  0.5917809, -0.10136628]))


def test_aitchison():
    test_np = np.array([0.1, 0.3, 0.4, 0.2])
    assert np.allclose(aitchison(test_np, test_np), 0.0)


def test_replace_zero_aitchison():
    test_np = np.array([0.1, 0, 0.4, 0.2])
    assert np.allclose(replace_zero_aitchison(test_np, test_np), 0.0)


def test_replace_zeroes():
    test_np = np.array([0.1, 0, 0, 0.2])
    assert np.array_equal(replace_zeroes(test_np),
                          np.array([0.1, 0.001, 0.001, 0.2]))
