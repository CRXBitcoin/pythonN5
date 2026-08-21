lengthOfSquarePacks = int(input("Enter the length of square packs being made: "))
if lengthOfSquarePacks > 0 and lengthOfSquarePacks < 10:
    widthOfSquarePacks = lengthOfSquarePacks

    specialOffer = input("Is a special offer running? (y/n): ")
    if specialOffer == "y":
        additionalRows = int(input("Please enter the number of additional rows included for free: "))
        widthOfSquarePacks = widthOfSquarePacks + additionalRows
        
totalNumberOfCans = lengthOfSquarePacks * widthOfSquarePacks
print("The number of cans in the pack is: "+str(totalNumberOfCans))