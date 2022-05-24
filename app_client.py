import entropy_stream
import apps

def get_blocks(N, T, p):
    blocks = []
    types = ["SHANNON", "RENYI", "MIN"]
    for t in types:
        if t != "SHANNON":
            blocks.append(entropy_stream.create_block_source(N, T, p, t))
        else: 
            blocks.append(entropy_stream.create_block_source(N, T, 1 / p, t))
    return blocks

def test_probing(blocks):
    print("Testing Linear Probing insertions to half capacity") 
    for block in blocks:
        table = apps.LinearProbing(20)
        elems = entropy_stream.sample_block_source(block)
        for elem in elems:
            table.insert(elem)
        print("load factor: ", table.get_load() / table.get_size())


def test_allocation(blocks):
    pass

def test_filter(blocks):
    pass

def main():
    blocks = get_blocks(10, 10, 0.5)
    test_probing(blocks)
    test_allocation(blocks)
    test_filter(blocks)

if __name__=="__main__":
    main()
