from types import *

def create_hashtable(hash_function, capacity):
    if capacity < 2:
        raise ValueError('Capacity must be greater than 1.')
    else:
        entries = [None] * capacity
        return HashTable(entries, 0, capacity, hash_function)

def put(hash_table, key, value):
    index = hash_table.hash_func(key) % hash_table.capacity
    start = index
    while hash_table.table[index] is not None and hash_table.table[index].key != key:
        index = (index + 1) % hash_table.capacity
        if index == start:
            raise Exception('Hashtable is full.')
    if hash_table[index] is None:
        hash_table.table[index] = Entry(key, value)
        hash_table.size += 1
    else:
        hash_table.table[index].value = value
    return True

def get(hash_table, key):
    index = hash_table.hash_func(key) % hash_table.capacity
    start = index
    while hash_table.table[index] is not None and hash_table.table[index].key != key:
        index = (index + 1) % hash_table.capacty
        if index == start:
            raise Exception('Hashtable has no such key.')
    return hash_table.table[index].value

def contains(hash_table, key):
    index = hash_table.hash_func(key) % hash_table.capacity
    start = index
    while  hash_table.table[index] is not None and hash_table.table[index].key != key:
        index = (index + 1) % hash_table.capacty
        if index == start:
            return False
    return hash_table.table[index] is not None

#open addressing and linear probing
