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

    if (not contains(myset, element)):

        index = start_index
        while index < len(table) and table[index] != None:

            index += 1

            # increment
            if (index >= len(table)):
                index = 0
                
            # check if looping again
            if (index == start_index):
                raise Exception("table is full")
            
        # all can be simplified with index = (index + 1) % capacity

        table[index] = element
        print(table)

def contains(myset, element):
    hash_func = myset[0]
    table = myset[1]
    hashcode = hash_func(element)
    start_index = hashcode % len(table)

    index = start_index
    while index < len(table) and table[index] != element:

        index += 1

        # increment
        if (index >= len(table)):
            index = 0
            
        # check if looping again
        if (index == start_index):
            return False

    return True

def main():
    #myset = make_myset(5)
    myset = make_myset(5, bad_hash)
    table = myset[1]
    print(table)
    add(myset, "one")
    add(myset, "two")
    add(myset, "three")
    add(myset, "four")
    add(myset, "four")
    add(myset, "one")
    add(myset, "five")
    #add(myset, "six")
    print(table)
    print(contains(myset, "three"))
    print(contains(myset, "sixty"))

if __name__ == '__main__':
    main()