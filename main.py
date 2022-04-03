from OpenAddressing import OpenAddressing

import HashFunctions
import random

OpenHash = OpenAddressing(150, "Division", "Linear")

item_to_delete = random.randrange(0,3000)
item_to_find = random.randrange(0,3000)

print("Item to find is " + str(item_to_find) + " and item to delete is " + str(item_to_delete))

print("OPEN HASHING")
HashFunctions.hash_evaluation(OpenHash, "Data/dataset(150).txt", item_to_delete, item_to_find)

print("CHAIN HASHING")
