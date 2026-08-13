#Student ID: 011512781
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

hub = "hub" #where western resides. base point

group1 = [packages[12], packages[13], packages[14], packages[15], packages[18], packages[19], packages[33], packages[38]] #8, has to be on the same truck/delievered together
group2 = [packages[0], packages[3], packages[6], packages[7], packages[28], packages[29], packages[30], packages[36], packages[39]] #9 time constraint
group3 = [packages[5], packages[24], packages[25], packages[27], packages[31]] #5 delayed arrival 0905 delievered by 1030
group4 = [packages[2], packages[4], packages[17], packages[35], packages[37]] #5, must be on truck 2
group5 = [packages[10], packages[11], packages[16], packages[21], packages[22], packages[23], packages[26], packages[34]] #8 truck1b 
group6 = [packages[1], packages[32], packages[8], packages[9], packages[20]] #5 rest of truck 2


truck1 = Truck(
    0,
    []
)
truck2 = Truck(
    0, 
    []
)

truck1.packages_truck.extend(group1)
truck1.packages_truck.extend(group5)

truck2.packages_truck.extend(group3)
truck2.packages_truck.extend(group4)

#for package in truck1.packages_truck: checking to see if it worked
    #print(package.package_id)

#list containing truck route from, to. ex: hub -> 14, mileage. 
truck1_route = [
    (14, 1.9),
    ([15, 16, 34], 2.0),
    (22, 4.7),
    (24, 3.1),
    (19, 2.5),
    (20, 0.5),
    (17, 2.4),
    ([27, 35], 4.6),
    ([13, 39], 1.6),
    (12, 7.2),
    (23, 7.5),
    (11, 0.4),
    (hub, 6.4)
    ] #16
truck2_route = [
    ([40, 4], 3.6),
    (1, 1.1),
    ([30, 8], 4.5),
    ([37, 38, 5], 1.0),
    ([29, 7], 4.3),
    (hub, 3.8)
    ]

#remove truck2 packages from list here to do truck2b route
truck2b_route = [
    ([25, 26], 2.4),
    (6, 7.2),
    ([31, 32], 1.5),
    (36, 3.4),
    (18, 4.0), 
    (21, 5.3),
    (28, 1.2),
    ([2, 33], 1.1),
    (3, 4.8),
    (9, 0.6),
    (10, 2.8),
    (hub, 5.0)
    ]

#create truck time start at 8 am. 8X60 so that we can calculate hours/minutes conversion later
truck1_time = 8 * 60

for miles in truck1_route:
    truck1.cur_mile += miles[1]

    travel_time = (miles[1] / 18) * 60
    truck1_time += travel_time #have to convert this to time
  
    if miles[0] == hub:
        pass
    elif isinstance(miles[0], list): #isinstance a function call. isinstance(object, type)
        for i in range(len(miles[0])):
            package = hash_table.lookup(miles[0][i]) #variable nested indexing. variable[x][x]
            package.delivery_time = truck1_time
            package.status = "Delivered"
    else:
        package = hash_table.lookup(miles[0])
        package.delivery_time = truck1_time
        package.status = "Delivered"

truck2_time = 8 * 60

for miles in truck2_route:
    truck2.cur_mile += miles[1]

    travel_time = (miles[1] / 18) * 60
    truck2_time += travel_time #have to convert this to time
  
    if miles[0] == hub:
        pass
    elif isinstance(miles[0], list): #isinstance a function call. isinstance(object, type)
        for i in range(len(miles[0])):
            package = hash_table.lookup(miles[0][i]) #variable nested indexing. variable[x][x]
            package.delivery_time = truck2_time
            package.status = "Delivered"
    else:
        package = hash_table.lookup(miles[0])
        package.delivery_time = truck2_time
        package.status = "Delivered"


for miles in truck2b_route:
    truck2.cur_mile += miles[1]

    travel_time = (miles[1] / 18) * 60
    truck2_time += travel_time #have to convert this to time
  
    if miles[0] == hub:
        pass
    elif isinstance(miles[0], list): #isinstance a function call. isinstance(object, type)
        for i in range(len(miles[0])):
            package = hash_table.lookup(miles[0][i]) #variable nested indexing. variable[x][x]
            package.delivery_time = truck2_time
            package.status = "Delivered"
    else:
        package = hash_table.lookup(miles[0])
        package.delivery_time = truck2_time
        package.status = "Delivered"

#print(truck1_cur_time) THIS IS CORRECT!!! YAY IT MATCHES THE PRE PLANNING



#terminal intuitive interface -> delivery status, delivery time, any package time, total mileage
print("WGUPUS Terminal Intuitive Interface\n1. View all packages at a specific time.\n2. View total mileage\n3. Exit")

choice = int(input("Pick which option you want. "))

while choice != 3:
    if choice == 1:
        time_frame = input("Enter a time frame (HH:MM - HH:MM) ")
        package_lookup = int(input("What package number? "))
        package_info = hash_table.lookup(package_lookup)
        print(package_info.status, package_info.delivery_time)
    elif choice == 2:
        print(truck1.cur_mile + truck2.cur_mile)
    else:
        pass
    choice = int(input("Pick which option you want. "))

