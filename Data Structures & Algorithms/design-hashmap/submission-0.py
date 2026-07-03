class MyHashMap:

    def __init__(self):
        # Creating our buckets // used prime number to have good distribution less collisions
        self.size = 2069

        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        # modding with the size (a prime #) so that it has even dist and happens in O(1)
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hashed = self._hash(key)
        bucket = self.buckets[hashed]

        for i, key_value in enumerate(bucket):
            if key_value[0] == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))

    def get(self, key: int) -> int:
        hashed = self._hash(key)
        bucket = self.buckets[hashed]

        for keys, value in bucket:
            if keys == key:
                return value
        
        return -1

    def remove(self, key: int) -> None:
        hashed = self._hash(key)
        bucket = self.buckets[hashed]

        for i, key_value in enumerate(bucket):
            if key_value[0] == key:
                bucket.pop(i)
                return 

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)