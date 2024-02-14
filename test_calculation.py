import pytest
from calculation import *


def test_getSootPercentage():
    assert(getSootPercentage(0), 0.0147)
    assert(getSootPercentage(1), 0.0303)
    assert(getSootPercentage(5.467948717), pytest.approx(0.1))
