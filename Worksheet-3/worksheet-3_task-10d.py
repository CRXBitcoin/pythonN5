number1 = 0
number2 = 1
number3 = 0
counter = 0
while counter < 100:
    print(str(number1))
    number3 = number1 + number2
    number1 = number2
    number2 = number3
    counter = counter + 1
