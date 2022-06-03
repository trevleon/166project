import random
import numpy as np
from numpy import linalg as LA

def compute_threshold(M, T, epsilon, type):
    """
    returns p value for given choice of entropy
    """
    if type == "4.6":
        K = (M * T ** 2) / (4 * epsilon ** 2)
        return 1 / K
    elif type == "4.7":
        K = (M * T ** 2) / epsilon
        return 1 / M + T / (epsilon * K)
    elif type == "4.10":
        K = max(M, np.sqrt(M * T / epsilon))
        return 1 / M + 1 / K + np.sqrt((2 * T) / (epsilon * M)) * (1 / K)
    else:
        raise NotImplemented("passed in invalid entropy type")

def create_block_source(N, T, p):
    """
    T: size of random variables sequence in block
    p: threshold denoting described probability per block
        - min: p = max prob per block
        - renyi: p = collision probability per block

    Return: a 2d array of size TxN where row i represents the distribution of X_i
    """
    t = 0
    dist = np.zeros(N)
    prev_dist = np.zeros(N)  # need to keep this in case condition fails
    block = np.zeros(N)
    while (t < T):
        dist += np.random.uniform(0, 1, N)
        dist /= np.sum(dist)
        # print("distribution: ", dist)
        # print("collision probability: ", LA.norm(dist)**2) 
        if LA.norm(dist)**2 <= p: 
            prev_dist = dist
            block = np.vstack((block, dist)) 
            t += 1     
        else:
            dist = prev_dist
    return block[1:]

def sample_block_source(block):
    vals = np.zeros(block.shape[0])
    for i in range(block.shape[0]): 
        vals[i] = np.random.choice(range(block.shape[1]), 1, p=np.array(block[i,:]))
    return vals
