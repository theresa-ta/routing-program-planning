from packages import packages
from hash_table import HashTable

hash_table = HashTable() #class HashTable just creates a blueprint. in order to use, build the object. variable hash_table builds object HashTable() from class HashTable

for package in packages: #iterates through the list packages in packages.py
    hash_table.insert(package)

#print(hash_table.table[1].package_id) --> test to see if it worked. 

"""
Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:

•   delivery address

•   delivery deadline

•   delivery city

•   delivery zip code

•   package weight

•   delivery status (i.e., delayed, at the hub, en route, or delivered), including the delivery time
so am i creating a search here?
"""

#package_test = hash_table.lookup(1)
#print(package_test.package_id)
#print(package_test.status)