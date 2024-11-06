class HashTable:
    def __init__(self, size=10):
        # Initialize hash table with a fixed size
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists for chaining to handle collisions
    
    def hash_function(self, key):
        # Simple hash function using modulo operator
        return key % self.size
    
    def insert(self, key, value):
        # Insert key-value pair into the hash table
        index = self.hash_function(key)  # Compute the hash index
        # Check if key already exists, update if present
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update value if key exists
                return
        # Append new key-value pair if key does not exist
        self.table[index].append((key, value))
    
    def search(self, key):
        # Search for a value by key in the hash table
        index = self.hash_function(key)  # Compute the hash index
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value if key is found
        return None  # Return None if key is not found
    
    def delete(self, key):
        # Delete a key-value pair from the hash table
        index = self.hash_function(key)  # Compute the hash index
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair if key is found
                return True
        return False  # Return False if the key is not found


# Test the HashTable implementation

# Create a new hash table
hash_table = HashTable(size=10)

# Insert key-value pairs
hash_table.insert(1, 'apple')
hash_table.insert(2, 'banana')
hash_table.insert(3, 'cherry')

# Search for inserted keys
print("Search for key 1:", hash_table.search(1))  # Expected: 'apple'
print("Search for key 2:", hash_table.search(2))  # Expected: 'banana'
print("Search for key 3:", hash_table.search(3))  # Expected: 'cherry'

# Insert a key that already exists (update the value)
hash_table.insert(2, 'blueberry')
print("Search for key 2 after update:", hash_table.search(2))  # Expected: 'blueberry'

# Delete a key
print("Delete key 2:", hash_table.delete(2))  # Expected: True
print("Search for key 2 after deletion:", hash_table.search(2))  # Expected: None

# Try deleting a non-existing key
print("Delete key 10 (non-existing):", hash_table.delete(10))  # Expected: False

# Insert more elements to test collisions
hash_table.insert(11, 'grape')  # This will hash to the same index as key 1
hash_table.insert(21, 'kiwi')   # This will hash to the same index as key 1
print("Search for key 11:", hash_table.search(11))  # Expected: 'grape'
print("Search for key 21:", hash_table.search(21))  # Expected: 'kiwi'

# Check the hash table state for debugging purposes
print("Current table:", hash_table.table)