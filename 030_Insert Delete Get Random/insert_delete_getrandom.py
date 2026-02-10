import random
class RandomizedSet(object):

    def __init__(self):
        self.items_list = []
        self.items_map = {}
        

    def insert(self, val):
        if val not in self.items_map:
            self.items_list.append(val)
            self.items_map[val] = len(self.items_list) - 1
            return True
        else:
            return False
        
    def remove(self, val):
        if val in self.items_map:
            val_index = self.items_map[val]
            last_list_value = self.items_list[-1]

            self.items_list[val_index] = last_list_value
            self.items_map[last_list_value] = val_index
            
            del self.items_map[val]
            self.items_list.pop()
            return True

        else:
            return False
        
    def getRandom(self):
        if len(self.items_list):
            return random.choice(self.items_list)
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
