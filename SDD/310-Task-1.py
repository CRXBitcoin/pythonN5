print("Yearly Saving Plan")
monthly_savings_amount = []
total = 0
for counter in range (0,12):
    monthly_savings_amount.append(int(input("Enter the monthly savings amount for month " + str(counter + 1) + ": ")))
    total += monthly_savings_amount[counter]
    print("Total savings so far: ", total)
print("")
print("Total yearly savings: ", total)