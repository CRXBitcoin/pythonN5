name = input("Enter your name: ")
year = input("Enter the year of high school you are in (Ex: 1st, 2nd, 3rd, 4th, 5th, 6th): ")

while year != "1st" and year != "2nd" and year != "3rd" and year != "4th" and year != "5th" and year != "6th":
    print("Invalid input. Please enter a valid year (1st, 2nd, 3rd, 4th, 5th, or 6th).")
    year = input("Year Invalid. Enter the year of high school you are in (Ex: 1st, 2nd, 3rd, 4th, 5th, 6th): ")

print("Hello, " + name + "! You are in your " + year + " year of high school.")