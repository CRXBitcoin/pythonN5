name = input("Enter your name: ")
gender = input("Enter your gender (male/female): ")

while gender != "male" and gender != "female":
    print("Invalid input. Please enter a valid gender (male or female).")
    gender = input("Enter your gender (male/female): ")

age = int(input("Enter your age: "))

while age < 0 or age > 120:
    print("Invalid input. Please enter a valid age (0-120).")
    age = int(input("Enter your age: "))