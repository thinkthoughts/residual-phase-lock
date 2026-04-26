# src/revise.py
import numpy as np

def gradient_like_revision(y, residual, lr=0.1):
    """
    Simple correction step
    """
    return y - lr * residual

def normalize_revision(y):
    """
    Optional stabilization
    """
    norm = np.linalg.norm(y)
    if norm == 0:
        return y
    return y / norm
