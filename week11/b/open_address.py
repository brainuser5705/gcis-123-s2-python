def bad_hash(element):
    return 0

def make_myset(length, hash_func = hash):
    table = [None] * length
    return (hash_func, table)

def add(myset, element):
    hash_func = myset[0]
    table = myset[1]
    hashcode = hash_func(element)
    start_index = hashcode % len(table)
    print(element, ":", start_index)

    # TODO:
    if not contains(myset,element):
        if table[start_index] == None:
            table[start_index] = element
        else:
            i = start_index + 1
            while i != start_index:
                if i == len(table):
                    i = 0
                if i == start_index:
                    raise Exception("the table is full")
                if table[i] == None:
                    table[i] = element
                    break
                i += 1
                    
def contains(myset, element):
    # hash_func = myset[0]
    table = myset[1]
    # hashcode = hash_func(element)
    # start_index = hashcode % len(table)

    # simple solution for now:
    return element in table

def main():
    myset = make_myset(5)
    #myset = make_myset(5, bad_hash)
    table = myset[1]
    print(table)
    add(myset, "one")
    add(myset, "two")
    add(myset, "three")
    add(myset, "four")
    add(myset, "four")
    add(myset, "one")
    add(myset, "five")
    add(myset, "six")
    print(table)
    print(contains(myset, "three"))
    print(contains(myset, "sixty"))

if __name__ == '__main__':
    main()