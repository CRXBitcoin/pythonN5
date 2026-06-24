print("Percentage Calculator v1.0.0")
original_price = int(input("What is the original price of the item? (in pounds) "))
discount = original_price * 0.20
final_price = original_price - discount
print("The final price of the item after the discount is " + str(final_price) + " pounds.")