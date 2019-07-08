# Basic hash table key/value pair
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Basic hash table
# All storage values should be initialized to None
class BasicHashTable:
    def __init__(self, capacity):
        # max. capacity of the Hash Table (how many key:value pairs it can take)
        self.capacity = capacity
        # underlying data storage:
        self.storage = [None] * capacity


# Research and implement the djb2 hash function
def hash(string):
    # hash(i) = hash(i - 1) * 33 ^ str[i];
    prime = 5381
    for c in string:
        prime = (prime * 33) + ord(c)
    return prime


# abstract away function to return an Index for hashed key
def get_idx(hash_table, key):
    return hash(key) % hash_table.capacity


# If you are overwriting a value with a different key, print a warning.
def hash_table_insert(hash_table, key, value):
    arr_idx = get_idx(hash_table, key)
    if hash_table.storage[arr_idx]:
        print(
            f'WARNING: Overwriting existing key: value pair.')

    hash_table.storage[arr_idx] = Pair(key, value)


# If you try to remove a value that isn't there, print a warning.
def hash_table_remove(hash_table, key):
    arr_idx = get_idx(hash_table, key)
    if not hash_table.storage[arr_idx]:
        print(f'Hash Table does not contain this key:value pair')
        return None
    else:
        hash_table.storage[arr_idx] = None


# Should return None if the key is not found.
def hash_table_retrieve(hash_table, key):
    arr_idx = get_idx(hash_table, key)
    if not hash_table.storage[arr_idx]:
        return None
    else:
        return hash_table.storage[arr_idx].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
