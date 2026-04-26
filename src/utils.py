# src/utils.py
import numpy as np

def seed_all(seed=0):
    np.random.seed(seed)

def make_toy_data(n=100):
    x = np.linspace(-1, 1, n)
    y = x**2
    return x.reshape(-1, 1), y.reshape(-1, 1)
