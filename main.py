# Building a Travel Weather Planner

distance_mi = int(input("Enter Distance That Have To Cover: "))
is_raining = bool(input("Raining or Not(Give Answer in True or False)"))
has_bike = bool(input("Has Bike or Not(Give Answer in True or False)"))
has_car = bool(input("Has Car or Not(Give Answer in True or False)"))
has_ride_share_app = bool(input("Has Ride Share App or Not(Give Answer in True or False)"))

# Check if distance is falsy
if not distance_mi:
    print(False)

elif distance_mi <= 1 and is_raining == False:
    print("True")

elif distance_mi <= 1 and is_raining == True:
    print("False")

elif 1 < distance_mi <= 6 and has_bike == True:
    print("True")

elif 1 < distance_mi <= 6 and has_bike == False:
    print("False")

elif distance_mi > 6 and has_car == True:
    print("True")

elif distance_mi > 6 and has_ride_share_app == True:
    print("True")

elif distance_mi > 6 and has_ride_share_app == False:
    print("False")

elif has_ride_share_app == True:
    print("Use Ride Share")

else:
    print("No Transport Available")