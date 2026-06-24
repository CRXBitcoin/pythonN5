print("Split-The-Bill.com v1.0.0")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    # Hello, You.
number_of_people = int(input("How many people are having a meal? "))
total_bill = float(input("What is the total bill? (in pounds) "))
tip = total_bill * 0.1
final_bill = total_bill + tip
cost_per_person = final_bill / number_of_people
print("The total bill including tip is " + str(final_bill) + " pounds.")
print("Each person should pay " + str(cost_per_person) + " pounds.")