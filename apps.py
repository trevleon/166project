import statistics as st
import random

class Entry: 
    def __init__(self, value): 
        self.value = value
        self.grave = False
class LinearProbing: 
    def __init__(self, size): 
        self.size = size
        self.table = [None for _ in range(size)]
        self.load = 0
        self.p = 2**61 - 1
        self.a = random.randint(1,p - 1)
        self.b = random.randint(0, p - 1)
    
    def hash(self, value): 
        return (self.a * value + self.b) % self.p % self.size

    def insert(self, value):
    
        index = self.hash(value)
        for i in range(self.size):
            if self.table[index + i] == None or self.table[index + i].grave == True: 
                self.table[index + i] = Entry(value)
                self.load += 1
                return i 
    def remove(self, value): 
        index = self.hash(value)
        for i in range(self.size):
            if self.table[index + i] != None and self.table[index + i].grave == False and self.table[index + i].value == value:
                self.table[index + i].grave = True
                self.load -= 1
                return i 
    def get_load(self): 
        return self.load
    def get_size(self): 
        return self.size

class BalancedAllocation: 
    def __init__(self, size, k):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.elems = 0
        self.p = 2**61 - 1
        self.a = [random.randint(1,self.p - 1) for _ in range(k)]
        
        self.k = k
    
    def hash(self, value): 
        hashes = []
        for _ in range(self.k):
            sum = 0
            for i in range(self.k): 
                sum += a[i] * value**i
            hashes.append(sum % self.p & self.size)
        return hashes
            
    def insert(self, value): 
        hash_indices = self.hash(value)
        loads = []
        for index in hash_indices: 
            loads.append(len(self.table[index]))
        self.table[loads.index(min(loads))].append(Entry(value))
        self.elems += 1

    def remove(self, value):
        hash_indices = self.hash(value)
        for index in hash_indices: 
            if value in self.table[index]: 
                self.table[index].pop(self.table[index].index(value))
                self.elems += 1
                return index

    def get_min_load(self): 
        min_index = 0
        for i in range(self.size):
            if len(self.table[i]) < len(self.table[min_index]):
                min_index = i

        return len(self.table[min_index])

    def get_mean_load(self): 
        return self.elems / self.size

    def get_median_load(self): 
        loads = []
        for i in range(self.size): 
            loads.append(len(self.table[i]))
        return st.median(loads)
        
    def get_max_load(self): 
        max_index = 0
        for i in range(self.size):
            if len(self.table[i]) > len(self.table[max_index]):
                max_index = i

        return len(self.table[max_index])

class BloomFilter: 
    def __init__(self, size, k):
        self.size = size
        self.table = [0 for _ in range(size)]
        self.p = 2**61 - 1
        self.a = [random.randint(1,self.p - 1) for _ in range(k)]
        self.k = k

    def hash(self, value): 
        hashes = []
        for _ in range(self.k):
            sum = 0
            for i in range(self.k): 
                sum += self.a[i] * value**i
            hashes.append(sum % self.p & self.size)
        return hashes

    def insert(self, value):
        hash_indices = self.hash(value)
        for index in hash_indices: 
            self.table[index] = 1

    def contains(self, value): 
        hash_indices = self.hash(value)
        for index in hash_indices: 
            if self.table[index] == 0: 
                return False
        return True
    
