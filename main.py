#Student ID: 011512781

#import files 
from packages import packages
from hash_table import HashTable

#class HashTable just creates a blueprint. in order to use, build the object. variable hash_table builds object HashTable() from class HashTable
hash_table = HashTable() 

#iterates through the list packages in packages.py to insert each object/package into the hash table using ID. 
for package in packages: 
    hash_table.insert(package)

#print(hash_table.table[1].package_id) --> test to see if it worked. 

#package_test = hash_table.lookup(1) --> test. it worked
#print(package_test.package_id)
#print(package_test.status)

#terminal intuitive interface -> delivery status, delivery time, any package time, total mileage
print("WGUPUS Terminal Intuitive Interface\n1. Look up package\n2. View total mileage\n3. Exit")

choice = int(input("Pick which option you want."))

while choice != 3:
    if choice == 1:
        package_lookup = int(input("What package number?"))
        package_info = hash_table.lookup(package_lookup)
        print(package_info.status, package_info.delivery_time)
    elif choice == 2:
        pass #havnt created truck so nothing is keeping track of mileage right now
    else:
        pass