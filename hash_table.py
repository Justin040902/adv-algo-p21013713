# hash_table.py
class Node:
    """Node for linked list in separate chaining"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """Hash Table implementation using separate chaining"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def _hash(self, key):
        """Simple hash function using modulo division"""
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        return key % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table"""
        index = self._hash(key)
        
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            
            if current.key == key:
                current.value = value
            else:
                current.next = Node(key, value)
        
        self.count += 1
    
    def search(self, key):
        """Search for a key in the hash table"""
        index = self._hash(key)
        current = self.table[index]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def display(self):
        """Display all elements in the hash table"""
        for i in range(self.size):
            print(f"Bucket {i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"[{current.key}: {current.value.name}] -> ", end="")
                current = current.next
            print("None")