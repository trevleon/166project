import entropy_stream
import apps
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import math

<<<<<<< HEAD
def get_blocks(n, T, m, epsilon):
    k = m + 2 * np.log2(T / epsilon)
    # k = 2
    blocks = []
    types = ["RENYI", "MIN", "SHANNON"]
    for t in types: 
            blocks.append(entropy_stream.create_block_source(n, T, entropy_stream.compute_threshold(k, t, n, epsilon), t))
=======
def get_blocks(n, T, m, epsilon, type):
    #k = m + 2 * np.log2(T / epsilon)
    #k = 
    k = 2
    blocks = []
    types = ["SHANNON", "RENYI", "MIN"]
    #for t in tqdm(types): 
    blocks.append(entropy_stream.create_block_source(n, T, entropy_stream.compute_threshold(k, types[type]), types[type]))
    
>>>>>>> c882f93e0d0f5952df321f224a2902ab279e84d2
    return blocks
def get_blocks_probing(n, T, m, epsilon, type):
    #k = 2
    k = 4 * math.log2(m)
    blocks = []
    types = ["SHANNON", "RENYI", "MIN"]
    #for t in tqdm(types): 
    blocks.append(entropy_stream.create_block_source(n, T, entropy_stream.compute_threshold(k, types[type]), types[type]))
    


def test_probing():
    print("Testing Linear Probing insertions to half capacity")
    blocks = get_blocks(10, 10, 20, .01)
    for block in blocks:
        table = apps.LinearProbing(20)
        elems = entropy_stream.sample_block_source(block)
        for elem in elems:
            table.insert(elem)
        print("load factor: ", table.get_load() / table.get_size())


def test_allocation():
    print("Testing Balanced Allocation")
    blocks = get_blocks(10, 10, 20, .1)
    for block in blocks:
        # not really sure how to use/test this one, but here's an
        # initialized class with m=20, d=2
        var_name = apps.BalancedAllocation(20, 2)
        # elems is an array of 10 elements to hash, of the form
        # [7. 6. 2. 7. 8. 7. 5. 4. 5. 3.] 
        elems = entropy_stream.sample_block_source(block)

def test_filter():
    print("Testing Bloom Filter")
    blocks = get_blocks(10, 10, 20, .1)
    for block in blocks:
        # not really sure how to use/test this one either, but here's an
        # initialized class with m=20, l=2
        var_name = apps.BloomFilter(20, 2)
        # elems is an array of 10 elements to hash, of the form
        # [7 6 2 7 8 7 5 4 5 3] 
        elems = entropy_stream.sample_block_source(block)

def linear_probing_data(t): 
    datas = []
    for _ in range(1): 
        blocks = get_blocks(200,200,20,.01, t)
        for block in (blocks):
            data = [] 
            table = apps.LinearProbing(200)
            elems = entropy_stream.sample_block_source(block)
            for elem in elems: 
                data.append(table.insert(elem))
            datas.append(data)
    return datas
    ret = []
    for i in range(len(datas[0])):
        sum = 0
        for d in datas: 
            sum += d[i]
        ret.append(sum / len(datas[0]))
    return ret
def balanced_data(t): 
    datas = []
    for _ in range(10): 
        blocks = get_blocks(10,100,20,.01, t)

        for block in blocks: 
            data = []
            table = apps.BalancedAllocation(200)
            elems = entropy_stream.sample_block_source(block)
            for elem in elems: 
                table.insert(elem)
                data.append(table.get_median_load())
            datas.append(data)
    return datas
def bloom_data(t): 
    datas = []
    for _ in range(10):
        blocks = get_blocks(10,100,20,.01, t)

        for block in blocks: 
            data = []
            elems_1 = entropy_stream.sample_block_source(block)
            elems_2 = entropy_stream.sample_block_source(block)
            bloom = apps.BloomFilter(200)
            for elem in elems_1: 
                bloom.insert(elem)
            fp_count = 0
            for elem in elems_2: 
                if elem not in elems_1 and bloom.contains(elem): 
                    fp_count += 1
            data.append(fp_count)
        datas.append(data)
    return datas
                





def main():
    #test_probing()
    #test_allocation()
    #test_filter()
    data = linear_probing_data(1)
    x = [i for i in range(len(data))] 
    plt.plot(x, data[0])
    plt.show()


if __name__=="__main__":
    main()
