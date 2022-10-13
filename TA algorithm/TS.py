from pickle import FALSE
import numpy as np


def generate_threshold_sequence(m, n, D_full, n_i, f):
    t = np.arange(2*n_i)
    for i in t:
        index = np.random.choice(np.arange(D_full.shape[0]),n,False)
        D = D_full[index,:]
