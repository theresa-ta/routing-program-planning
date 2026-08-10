#Student ID: 011512781

#import files 
from packages import packages
from hash_table import HashTable
from truck import Truck

#class HashTable just creates a blueprint. in order to use, build the object. variable hash_table builds object HashTable() from class HashTable
hash_table = HashTable() 

#iterates through the list packages in packages.py to insert each object/package into the hash table using ID. 
for package in packages: 
    hash_table.insert(package)

#print(hash_table.table[1].package_id) --> test to see if it worked. 

#package_test = hash_table.lookup(1) --> test. it worked
#print(package_test.package_id)
#print(package_test.status)

group1 = [packages[12], packages[13], packages[14], packages[15], packages[18], packages[19], packages[20], packages[33], packages[38]] #9, has to be on the same truck/delievered together
group2 = [packages[0], packages[3], packages[6], packages[7], packages[28], packages[29], packages[30], packages[36], packages[39]] #9 time constraint
group3 = [packages[5], packages[24], packages[25], packages[27], packages[31]] #5 delayed arrival 0905 delievered by 1030
group4 = [packages[2], packages[4], packages[17], packages[35], packages[37]] #5, must be on truck 2
group5 = [packages[10], packages[11], packages[16], packages[21], packages[22], packages[23], packages[26], packages[34]] #8 truck1b 
group6 = [packages[1], packages[32], packages[8], packages[9]] #4 rest of truck 2


truck1 = Truck(
    0,
    []
)
truck2 = Truck(
    0, 
    []
)

#terminal intuitive interface -> delivery status, delivery time, any package time, total mileage
print("WGUPUS Terminal Intuitive Interface\n1. Look up package\n2. View total mileage\n3. Exit")

choice = int(input("Pick which option you want."))

while choice != 3:
    if choice == 1:
        package_lookup = int(input("What package number?"))
        package_info = hash_table.lookup(package_lookup)
        print(package_info.status, package_info.delivery_time)
    elif choice == 2:
        pass #truck mileage not implemented yet 
    else:
        pass
    choice = int(input("Pick which option you want."))