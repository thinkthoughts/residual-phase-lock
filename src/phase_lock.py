# src/phase_lock.py
import numpy as np

PHASE_LOCK_THRESHOLD = 1 / np.sqrt(2)

def cosine_alignment(a, b, eps=1e-8):
    """
    cos(theta) between two vectors
    """
    return np.dot(a, b) / ((np.linalg.norm(a) * np.linalg.norm(b)) + eps)

def is_phase_locked(a, b):
    """
    Returns True if alignment passes threshold
    """
    cos_theta = cosine_alignment(a, b)
    return cos_theta >= PHASE_LOCK_THRESHOLD, cos_theta
