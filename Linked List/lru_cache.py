class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Let's try a doubly linkedlist for maintaing order for O(1) access for put
# Use cache for O(1) access for get()
class LRUCache:
    def __init__(self, capacity: int):
        self.old = Node(0, 0) #dummy node
        self.new = Node(0, 0) #dummy node
        self.old.next = self.new
        self.new.prev = self.old

        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev, next = self.new.prev, self.new

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

        

    def put(self, key: int, value: int) -> None:
        # Update value of 'key' if key exists, make sure its now the newest
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # Replace oldest item in the cache
        if len(self.cache) > self.capacity:
            lru = self.old.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
