# src/models.py
import numpy as np

class LinearModel:
    def __init__(self, w):
        self.w = w

    def __call__(self, x):
        return x @ self.w


class NonlinearModel:
    def __call__(self, x):
        return np.tanh(x)
