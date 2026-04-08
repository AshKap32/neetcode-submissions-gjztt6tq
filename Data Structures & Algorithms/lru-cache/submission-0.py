class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:

        if key in self.lru_cache:
            # Just used so move it to the end of the list
            self.lru_cache.move_to_end(key)
            return self.lru_cache[key]

        else:
            return -1



    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.lru_cache[key] = value 
            # Moving key to the end cuz just used it
            self.lru_cache.move_to_end(key)  
            return       
        elif self.capacity == len(self.lru_cache):
            # Popping the first item since it is the least recently used key
            self.lru_cache.popitem(last=False)

        # We update the key or add in either way, but we wanna first check
        # if it already exists, then we just update the value
        # ORdered DIct auto appends it at the last 
        self.lru_cache[key] = value

        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)