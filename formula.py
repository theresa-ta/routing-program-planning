truck_speed = 16 #created a while loop to help get distance and time for each stop

while True:
    distance = float(input())

    if distance == -1:
        break
    
    travel_time = (distance / truck_speed) * 60
    minutes = int(travel_time)
    seconds = round((travel_time - minutes) * 60)
    print(f"{minutes} minutes, {seconds} seconds.") 
