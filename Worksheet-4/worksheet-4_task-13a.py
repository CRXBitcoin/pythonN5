Number = [""] * 5
for counter in range(0,5):
    print("Please enter a number:")
    number = int(input())
    Number[counter] = number
print("The numbers you entered are: ", Number[0], Number[1], Number[2], Number[3], Number[4])