import entropy_stream
import apps
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import math

# types = ["SHANNON", "RENYI", "MIN"]
types = ["4.6", "4.7", "4.10"]

def get_blocks(N, M, T, epsilon):
    blocks = []
    for  type in types:
        p = entropy_stream.compute_threshold(M, T, epsilon, type)
        print(p, ">?", 1 / N)
    # for t in tdqm(types):
        blocks.append(entropy_stream.create_block_source(N, T, p))
    return blocks

"""
def get_blocks_probing(N, T, M, epsilon, type):
    #k = 2
    k = 4 * math.log2(M)
    blocks = []
    types = ["SHANNON", "RENYI", "MIN"]
    #for t in tqdm(types): 
    p = entropy_stream.compute_threshold(M, T, epsilon, types[type])
    blocks.append(entropy_stream.create_block_source(N, T, p, types[type]))
    return blocks
"""

def test_probing():
    print("Testing Linear Probing insertions to half capacity")
    blocks = get_blocks(10, 10, 20, .01, 1)
    table = apps.LinearProbing(20)
    for block in blocks:
        elems = entropy_stream.sample_block_source(block)
        for elem in elems:
            table.insert(elem)
        print("load factor: ", table.get_load() / table.get_size())

def test_allocation():
    print("Testing Balanced Allocation")
    blocks = get_blocks(10, 10, 20, .1, 1) 
    # not really sure how to use/test this one, but here's an
    # initialized class with m=20, d=2
    var_name = apps.BalancedAllocation(20, 2)
    # elems is an array of 10 elements to hash, of the form
    # [7. 6. 2. 7. 8. 7. 5. 4. 5. 3.] 
    for block in blocks:
        elems = entropy_stream.sample_block_source(block)

def test_filter():
    print("Testing Bloom Filter")
    blocks = get_blocks(10, 10, 20, .1, 1) 
    # not really sure how to use/test this one either, but here's an
    # initialized class with m=20, l=2
    var_name = apps.BloomFilter(20, 2)
    # elems is an array of 10 elements to hash, of the form
    # [7 6 2 7 8 7 5 4 5 3] 
    for block in blocks:
        elems = entropy_stream.sample_block_source(block)

def linear_probing_data():
    datas = []
    for _ in range(1): 
        blocks = get_blocks(1000000, 25, 15, 1 / (15**1.01)) 
        data = []
        table = apps.LinearProbing(20)
        for block in blocks:
            elems = entropy_stream.sample_block_source(block) 
            print("curr")
            for elem in elems: 
                data.append(table.insert(elem))
            print(data)
            datas.append(data)
    return datas
    ret = []
    for i in range(len(datas[0])):
        sum = 0
        for d in datas: 
            sum += d[i]
        ret.append(sum / len(datas[0]))
    return ret

def balanced_data(): 
    datas = []
    for _ in range(10): 
        blocks = get_blocks(10,100,20,.01)
        data = []
        table = apps.BalancedAllocation(200)
        for block in blocks:
            elems = entropy_stream.sample_block_source(block)
            for elem in elems: 
                table.insert(elem)
                data.append(table.get_median_load())
            datas.append(data)
    return datas

def bloom_data(): 
    datas = []
    for _ in range(10):
        blocks = get_blocks(10,100,20,.01)
        data = []
        for block in blocks:
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
    data = linear_probing_data()
    x = [i for i in range(len(data))]
    plt.plot(x, data)
    plt.show()


if __name__=="__main__":
    main()
