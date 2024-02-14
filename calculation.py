def getSootPercentage(absorbance: float) -> float:
    """Returns the soot percentage for a given absorbance"""

    sootPercentage = (0.0156 * absorbance) + 0.0147

    return sootPercentage


def getSootAbsorbance(sootPercentage: float) -> float:
    """Returns the expected absorbance for a given soot percentage"""

    sootAbsorbance = (sootPercentage - 0.0147) / 0.0156

    return sootAbsorbance
