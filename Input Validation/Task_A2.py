name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
while age < 11 or age > 18:
    print("Too young/old. Please enter an age between 11 and 18.")
    age = int(input("Enter your age: "))
print("Hello ", name,", you have entered the talent show!")