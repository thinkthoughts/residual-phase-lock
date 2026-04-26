# src/residuals.py
import numpy as np

def l2_residual(y, target):
    """Basic L2 residual"""
    return np.linalg.norm(y - target)

def relative_residual(y, target, eps=1e-8):
    """Scale-invariant residual"""
    return np.linalg.norm(y - target) / (np.linalg.norm(target) + eps)

def structured_residual(y, target):
    """
    Placeholder for domain-specific residuals:
    - zeta: spacing / ratio mismatch
    - ML: logical / constraint violation
    """
    return y - target
