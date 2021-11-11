class Entry:
    """
    Each entry consist of a key and value.
    """

    #TODO: 
    pass

class HashTable:
    """
    A hashtable has the following attributes:
    - capacity: the size limit of the hash table
    - hash: the hash function to use
    - table: the structure used to store Entry objects

    You can perform the following operations with the hash table:
    - put, contains, and get
    """
    
    #TODO: Write the constructor

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
        """
        Puts a key and value pair (Entry) into the hash table, using open addressing if any collisions.
        Raises an exception if hash table is full.
        """
        #TO DO:

        pass

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




