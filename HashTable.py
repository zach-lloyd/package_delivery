class HashTable:
    def __init__(self, buckets = 40):
        """
        Called upon creation of an object.
        
        :param buckets: The number of buckets the hash table should have.
        """
        self.table = []
        
        for i in range(buckets):
            self.table.append([])
    
    def _get_hash(self, key):
        """
        Hashes a key to determine the appropriate bucket for the specified
        key.
        
        :param key: The key to be hashed.
        """
        bucket = int(key) % len(self.table)
        return bucket

    def __iter__(self):
        """
        Generator to iterate through all the items in the hash table.
        """
        for bucket in self.table:
            for key_value in bucket:
                yield key_value[1]
    
    def insert(self, key, item):
        """
        Inserts a key-value pair into the hash table. Uses chaining to handle 
        collisions. 
        
        :param key: The key to be inserted. 
        :param item: The associated value.
        """
        bucket = self._get_hash(key)
        bucket_list = self.table[bucket]

        # Update if key already exists in this bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        
        # If not found, insert the item at the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
    
    def lookup(self, key):
        """
        Looks up a key in the hash table.
        
        :param key: The key to be looked up.
        """
        bucket = self._get_hash(key)
        bucket_list = self.table[bucket]

        # Search for the key in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1] # Returns the Package object
            
        return None  # Not found


    