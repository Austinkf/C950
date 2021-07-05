# Create a hash table
class HashTable:
    # Initialize hash table with a capacity of 50
    def __init__(self, init_cap=50):
        self.table = [None] * init_cap

    # Creates the hash keys
    def get_key(self, key):
        bucket = int(key) % len(self.table)
        return bucket

    # Inserts a new value into the table
    def insert(self, key, value):
        key_hash = self.get_key(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.table[key_hash].append(key_value)
            return True

    # Updates values on the table
    def update(self, key, value):
        key_hash = self.get_key(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print("Could not update the key " + key + " please try again")

    # Searches for a key in the table and returns the value
    def search(self, key):
        key_hash = self.get_key(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Deletes entry from the table
    def delete(self, key):
        key_hash = self.get_key(key)

        if self.table[key_hash] is None:
            return False
        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
        return False
