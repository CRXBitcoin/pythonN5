numberofbadges = 0
startingprice = 25
print("Badge Store")
numberofbadges = int(input("How many badges would you like to buy? "))
if numberofbadges > 150:
    print("Discount applied! You will receive a 10% discount on your purchase.")
    totalcost = numberofbadges * startingprice * 0.9
else:
    totalcost = numberofbadges * startingprice
totalcost = totalcost/100
totalcost = round(totalcost, 2)
print("Total cost: £", totalcost)