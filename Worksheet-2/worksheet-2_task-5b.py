print("The Equation Program")
print("")
print("Please select an option from the following menu:")
print("1. Calculate the speed")
print("2. Calculate the distance")
print("3. Calculate the time")
print("4. Calculate the area of a rectangular room")
print("5. Exit program")

option = int(input("Enter your option: "))

if option == 1:
    distance = float(input("Enter the distance (in meters): "))
    time = float(input("Enter the time (in seconds): "))
    speed = distance / time
    print(f"The speed is {speed} meters per second.")
elif option == 2:
    speed = float(input("Enter the speed (in meters per second): "))
    time = float(input("Enter the time (in seconds): "))
    distance = speed * time
    print(f"The distance is {distance} meters.")
elif option == 3:
    distance = float(input("Enter the distance (in meters): "))
    speed = float(input("Enter the speed (in meters per second): "))
    time = distance / speed
    print(f"The time is {time} seconds.")
elif option == 4:
    length = float(input("Enter the length of the room (in meters): "))
    width = float(input("Enter the width of the room (in meters): "))
    area = length * width
    print(f"The area is {area} square meters.")
elif option == 5:
    print("Exiting program.")
else:
    print("Invalid option. Please try again.")