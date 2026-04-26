# src/metrics.py
import numpy as np

def residual_norm(r):
    return np.linalg.norm(r)

def residual_mean(r):
    return np.mean(r)

def residual_std(r):
    return np.std(r)

def violation_score(r, threshold=1e-3):
    """
    Fraction of elements exceeding tolerance
    """
    return np.mean(np.abs(r) > threshold)
