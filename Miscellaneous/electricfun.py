startMiles = 0
journey = []
for index in range(0,3):
    currentMiles = int(input("Enter the mileage at the current charging station: "))
    kWRating = int(input("Enter the kW rating of the charging station: "))
    while kWRating < 7 or kWRating > 50:
        print("Invalid kW rating. Please enter a value between 7 and 50.")
        kWRating = int(input("Enter the kW rating of the charging station: "))
    if kWRating == 7:
        pricePerMile = 0
    else:
        if kWRating == 22:
            pricePerMile = 0.005
        else:
            pricePerMile = 0.01
    milesTravelled = currentMiles - startMiles
    startMiles = currentMiles
    journeyStage = pricePerMile * milesTravelled
    journey.append(journeyStage)
    print("The cost of this stage of the journey is: ", journeyStage)
print("The total cost of the journey is: ", sum(journey))