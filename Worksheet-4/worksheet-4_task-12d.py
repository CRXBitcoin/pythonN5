import random
import time

print("National Lottery Ticket Generator v1.0.0")

while True:
    print("First, pick 6 numbers between 1 and 59.")
    number1 = int(input("Pick your first number: "))
    number2 = int(input("Pick your second number: "))       
    number3 = int(input("Pick your third number: "))
    number4 = int(input("Pick your fourth number: "))
    number5 = int(input("Pick your fifth number: "))
    number6 = int(input("Pick your sixth number: "))
    print("")
    print("Your numbers are: ", number1, number2, number3, number4, number5, number6)
    print("")
    print("Confirm your numbers? (Y/N)")
    answer = input().upper()
    if answer == "Y":
        print("Beginning the lottery draw!")
        break
    print("Picking numbers again!")

counter = 1
number = 0
numberscorrect = 0
drawn_numbers = set()
while len(drawn_numbers) < 6:
    number = random.randint(1, 59)
    if number in drawn_numbers:
        continue
    drawn_numbers.add(number)
    time.sleep(1)
    print(number)
    if number == number1 or number == number2 or number == number3 or number == number4 or number == number5 or number == number6:
        numberscorrect += 1
else:
    print("You have completed the lottery draw!")

print("You got ", numberscorrect, " correct!")