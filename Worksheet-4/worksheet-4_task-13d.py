import random
Number = [""] * 100

for counter in range(0,100):
    number = random.randint(1, 100)
    print(number)
    Number[counter] = number

print("The numbers over 80 are: ")
for counter in range(0,100):
    if Number[counter] > 80:
        print(Number[counter])