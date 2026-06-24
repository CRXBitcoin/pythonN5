print("Monthly-Debt-Payment-Calculator v1.0.0")
print("How much money are you borrowing?")
amount_borrowed = float(input())
print("How many months would you like to repay the loan over?")
months_to_repay = float(input())
amount_borrowed_with_interest = amount_borrowed * 1.15
monthly_payment = amount_borrowed_with_interest / months_to_repay
print(f"Your monthly payment will be: {monthly_payment:.2f} pounds.")