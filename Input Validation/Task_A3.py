name = str(input("Enter your name: "))
house = str(input("Enter your school house (Stuart/Forbes/Douglas/Gordon): "))
while house != "Stuart" and house != "Forbes" and house != "Douglas" and house != "Gordon":
    print("Invalid school house. Please enter a valid school house (Stuart/Forbes/Douglas/Gordon).")
    house = str(input("Enter your school house (Stuart/Forbes/Douglas/Gordon): "))
school_house = [name, house]
print("Name: ", school_house[0], "House: ", school_house[1])