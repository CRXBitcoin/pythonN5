print("Apple-Cost-Calculator v1.0.0")
number_of_apples = int(input("How many apples are you purchasing? "))
price_per_apple = float(input("What is the price per apple? (in pounds) "))
total_cost = number_of_apples * price_per_apple
print("The total cost of the apples is " + str(total_cost) + " pounds.")