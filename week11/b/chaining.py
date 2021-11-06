def make_myset(length, hash_func = hash):
    table = [[] for n in range(length)]
    return (hash_func, table)

def add(myset, element):
    hash_func = myset[0]
    table = myset[1]
    hashcode = hash_func(element)
    index = hashcode % len(table)

    row = table[index]
    for set_element in row:
        if set_element == element:
            return
    row.append(element) # append element to the empty list in the table

def contains(myset, element):
    hash_func = myset[0]
    table = myset[1]
    hashcode = hash_func(element)
    index = hashcode % len(table)

    row = table[index]
    for set_element in row:
        if set_element == element:
            return True
    return False

def main():
    myset = make_myset(5)
    table = myset[1]
    print(table)
    add(myset, "one")
    add(myset, "two")
    add(myset, "three")
    add(myset, "four")
    add(myset, "four")
    add(myset, "one")
    print(table)
    print(contains(myset, "three"))
    print(contains(myset, "sixty"))

if __name__ == '__main__':
    main()