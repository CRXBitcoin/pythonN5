purpose = str(input("What is the purpose of the animation? "))
purpose = purpose.lower()
finalCost = basicCost

if purpose == "education":
    finalCost = finalCost - 20
elif purpose == "charity":
    finalCost = finalCost - 30

print (finalCost)