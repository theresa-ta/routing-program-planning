from packages import packages
from hash_table import HashTable

hash_table = HashTable() #class HashTable just creates a blueprint. in order to use, build the object. variable hash_table builds object HashTable() from class HashTable

for package in packages: #iterates through the list packages in packages.py
    hash_table.insert(package)

#print(hash_table.table[1].package_id) --> test to see if it worked. 