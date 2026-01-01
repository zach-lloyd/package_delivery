class HashTable:
    def __init__(self, buckets = 40):
        self.table = []
        for i in range(buckets):
            self.table.append([])
    
    def _get_hash(self, key):
        bucket = int(key) % len(self.table)
        return bucket
    
    def insert(self, key, item):
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
        bucket = self._get_hash(key)
        bucket_list = self.table[bucket]

        # Search for the key in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1] # Returns the Package object
        return None  # Not found


    