# Linked List hash table key/value pair
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Resizing hash table
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0
        self.load_factor = self.count / self.capacity


# Research and implement the djb2 hash function
def hash(string):
    prime = 5381
    for c in string:
        prime = (prime * 33) + ord(c)
    return prime


# abstract away function to return an Index for hashed key
def get_idx(hash_table, key):
    return hash(key) % hash_table.capacity


def hash_table_insert(hash_table, key, value):
    arr_idx = get_idx(hash_table, key)
    # collision
    if hash_table.storage[arr_idx]:
        print(
            f'Collision! Adding key:value pair "{key}: {value}" to the linked list')
        hash_table.storage[arr_idx].next = LinkedPair(key, value)
    # no collision
    else:
        hash_table.storage[arr_idx] = LinkedPair(key, value)
        hash_table.count += 1


# If you try to remove a value that isn't there, print a warning.
def hash_table_remove(hash_table, key):
    pass


# Should return None if the key is not found.
def hash_table_retrieve(hash_table, key):
    pass


def hash_table_resize(hash_table):
    new_capacity = hash_table.capacity * 2
    new_storage = [None] * hash_table.capacity

    for i in range(hash_table.count):
        new_storage[i] = hash_table.storage[i]

    hash_table.storage = new_storage
    hash_table.capacity = new_capacity


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")


"""
    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")

"""
Testing()
