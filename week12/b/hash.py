class Entry:

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value

class HashTable:
    
    def __init__(self, capacity, hash):
        self.__capacity = capacity
        self.__hash = hash
        self.__table = [None] * capacity

    def __get_index(self, key):
        hash_code = self.__hash(key)
        return (hash_code) % self.__capacity

    def contains(self, key):
        index = self.__get_index(key)
        start = index
        while self.__table[index] is not None and \
            self.__table[index].get_key() != key:
            index = (index + 1) % self.__capacity
            if index == start:
                return False
        return self.__table[index] is not None

    def get(self, key):
        index = self.__get_index(key)
        start = index
        while self.__table[index] is not None and \
            self.__table[index].get_key() != key:
            index = (index + 1) % self.__capacity
            if index == start:
                raise Exception('Hash table does not contain key:', key)
        if self.__table[index] is None:
            raise Exception('Hash table does not contain key:', key)
        else:
            return self.__table[index].get_value()

    def put(self, key, value):
        index = self.__get_index(key)
        start = index
        while self.__table[index] is not None and \
            self.__table[index].get_key() != key:
            index = (index + 1) % self.__capacity
            if index == start:
                raise Exception('Hash table is full')
        self.__table[index] = Entry(key, value)

    def __str__(self):
        string = "Printing: ["

        prefix = ""
        for entry in self.__table:
            if entry is not None:
                string += prefix + str(entry.get_value())
            else:
                string += "None "
            prefix = ", "
            
        string += "]"

        return string
 
def run_program():

    htable = HashTable(4, hash)

    htable.put("one", 1)
    print(htable)

    print(htable.contains("one"))
    print(htable.contains("two"))

    htable.put("two", 2)
    htable.put("three", 3)
    htable.put("four", 4)
    print(htable)

    print(htable.get("four"))
    print(htable.get("five"))

def main():
    run_program()

if __name__ == '__main__':
    main()      




