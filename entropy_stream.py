import random
import numpy as np
from numpy import linalg as LA
DEFAULT_SET_SIZE =5



def compute_threshold(k, entropy):
    if entropy == "SHANNON":
        return k    
    elif entropy == "RENYI" or entropy == "MIN":
        return 2 ** (-k)
    else:
        raise NotImplemented("passed in invalid entropy type")



def create_block_source(T, k, e_type):
    """
    T: size of random variables sequence in block
    k: threshold where
        - min: k = max prob
        - renyi: k = collision prob
        - shannon: k = min threshold entropy
    e_type: either min, Renyi, Shannon

    Return: a 2d array where row i represents the distribution of X_i
    """
    t = 0
    dist = np.zeros(DEFAULT_SET_SIZE)
    prev_dist = np.zeros(DEFAULT_SET_SIZE)  # need to keep this in case condition fails
    block = np.zeros(DEFAULT_SET_SIZE)
    while (t < T):
        dist += np.random.uniform(0, 1, DEFAULT_SET_SIZE)
        dist /= np.sum(dist)
        
        if (e_type == "RENYI" and LA.norm(dist)**2 <= k) or \
           (e_type == "MIN" and np.max(dist) <= k) or \
           (e_type == "SHANNON" and np.sum(dist * np.log(1/dist)) < k):
                prev_dist = dist
                block = np.vstack((block, dist)) 
                t += 1     
        else:
            dist = prev_dist
    print(block[1:])
    print("\n\n")
    return block[1:]




if __name__=="__main__":
    create_block_source(5, 2, "SHANNON")
    create_block_source(5, 0.5, "RENYI")
    create_block_source(5, 0.5, "MIN")