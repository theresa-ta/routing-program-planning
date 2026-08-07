truck_speed = 16 #created a while loop to help get distance and time for each stop. used for pre-planning

while True:
    distance = float(input())

    if distance == -1:
        break
    
    travel_time = (distance / truck_speed) * 60
    minutes = int(travel_time)
    seconds = round((travel_time - minutes) * 60)
    print(f"{minutes} minutes, {seconds} seconds.") 

""" steps to complete this assignment:
1. create class packages
2. insert package into hash tables
3. create class trucks
4. assign packages to trucks
5. nearest alogorithm 
6. update package status, mileage, + time
7. print results
"""