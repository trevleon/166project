import random
import numpy as np
from numpy import linalg as LA

def compute_threshold(k, entropy):
    if entropy == "SHANNON":
        return k    
    elif entropy == "RENYI" or entropy == "MIN":
        return 2 ** (-k)
    else:
        raise NotImplemented("passed in invalid entropy type")

def create_block_source(N, T, k, e_type):
    """
    T: size of random variables sequence in block
    k: threshold where
        - min: k = max prob
        - renyi: k = collision prob
        - shannon: k = min threshold entropy
    e_type: either min, Renyi, Shannon

    Return: a 2d array of size TxN where row i represents the distribution of X_i
    """
    t = 0
    dist = np.zeros(N)
    prev_dist = np.zeros(N)  # need to keep this in case condition fails
    block = np.zeros(N)
    while (t < T):
        dist += np.random.uniform(0, 1, N)
        dist /= np.sum(dist)
        
        if (e_type == "RENYI" and LA.norm(dist)**2 <= k) or \
           (e_type == "MIN" and np.max(dist) <= k) or \
           (e_type == "SHANNON" and np.sum(dist * np.log(1/dist)) < k):
                prev_dist = dist
                block = np.vstack((block, dist)) 
                t += 1     
        else:
            dist = prev_dist
    return block[1:]

def sample_block_source(block):
    vals = np.zeros(block.shape[0])
    for i in range(block.shape[0]): 
        vals[i] = int(np.random.choice(range(block.shape[1]), 1, p=np.array(block[i,:])))
    return vals
