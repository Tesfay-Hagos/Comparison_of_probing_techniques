import HashFunctions

class OpenAddressing:
    """Hash map using 'open addressing' to handle collisions. 
        It takes a desired hash function ('Division, Multiplication or Prime') 
        and desired probing method ('Linear, Quadratic or Double) as input"""
    def __init__(self, size ,hash_function, probe_mode):
        self.hash_function = hash_function
        self.probe_mode = probe_mode
        self.MAX = size
        self.hash_map = [None for i in range(self.MAX)]

    #MAIN FUNCTIONS (Set, Get and Delete items)
    def __setitem__(self, key, val):
        #Set an item / index in hash map to be found with the key and hold the value val
        if self.probe_mode == "Double":
            hash = HashFunctions.get_hash(key, self.MAX, "Division")
        else:
            hash = HashFunctions.get_hash(key, self.MAX, self.hash_function)
        
        if self.hash_map[hash] is None:
            self.hash_map[hash] = (key, val)
        else:
            new_h = self.find_open_slot(key, hash)
            self.hash_map[new_h] = (key,val)

    def __getitem__(self, key):
        #Takes a key as input, which it finds in the hash map, returning its corresponding value.
        hash = HashFunctions.get_hash(key, self.MAX, self.hash_function)
        if self.hash_map[hash] is None:
            return
        probing_range = self.get_probing_range(hash)
        for probe_index in probing_range:
            element = self.hash_map[probe_index]
            if element is None:
                print(str(element))
                return
            if element[0] == key:
                print(str(element))
                return element[1]

    def __delitem__(self, key):
        #Delete the given key and corresponding value from the hash map
        hash = HashFunctions.get_hash(key, self.MAX, self.hash_function)
        probing_range = self.get_probing_range(hash)
        for probe_index in probing_range:
            if self.hash_map[probe_index] is None:
                return
            if self.hash_map[probe_index][0] == key:
                print("Deletion successfull")
                self.hash_map[probe_index]= "Deleted"

    #HELPER FUNCTIONS (For assisting in finding new hash map indices in case of collision)
    def get_probing_range(self, index):
        #Set probing range to be from the index (hashed key) to the length of the hashmap, and from the start to the index
        return [*range(index, len(self.hash_map))] + [*range(0, index)]

    def find_open_slot(self, key, index):
        #Calculate a new hash map index in case of collision
        probing_range = self.get_probing_range(index)
        for probe_index in probing_range:
            
            if self.probe_mode == "Linear":
                probe_index = probe_index
            if self.probe_mode == "Quadratic":
                probe_index = (index + (probe_index**2)) % self.MAX
            if self.probe_mode == "Double":
                hash_2 = HashFunctions.get_hash(key, self.MAX, "Prime")
                probe_index = (index + (probe_index * hash_2)) % self.MAX
            
            if self.hash_map[probe_index] is None:
                return probe_index
            if self.hash_map[probe_index] == "Deleted":
                return probe_index
            if self.hash_map[probe_index][0] == key:
                return probe_index
        raise Exception("Hashmap is full!")