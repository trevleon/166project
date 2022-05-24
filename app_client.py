import entropy_stream
import apps
import numpy as np

def get_blocks(n, T, m, epsilon):
    # k = m + 2 * np.log2(T / epsilon)
    k = 2
    blocks = []
    types = ["SHANNON", "RENYI", "MIN"]
    for t in types: 
            blocks.append(entropy_stream.create_block_source(n, T, entropy_stream.compute_threshold(k, t), t))
    return blocks

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

def main():
    test_probing()
    test_allocation()
    test_filter()

if __name__=="__main__":
    main()
