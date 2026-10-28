import random

mystery_fruit = ["Apple", "Banana", "Blueberry", "Kiwi", "Mango", "Orange", "Peach", "Pineapple", "Raspberry", "Strawberry"]

fruit = []

fruit_juice = False
smoothie = False
milkshake = False

print("Welcome to Shake-Shake!")

number_of_fruits = int(input("How many fruits would you like in your drink? (1-6): "))
for i in range(number_of_fruits):
    print("Enter the name of fruit " + str(i + 1) + ": ")
    fruit_name = input()
    while len(fruit_name.strip()) < 4:
        print("Please enter a fruit name with at least 4 characters.")
        fruit_name = input()
    fruit_name = fruit_name.strip()  
    fruit_name = fruit_name.capitalize()  
    fruit.append(fruit_name)

fruit.append(random.choice(mystery_fruit))

number_of_fruits = number_of_fruits + 1

print("")

if number_of_fruits > 4:
    fruit_juice = True
elif number_of_fruits == 3 or number_of_fruits == 4:
    smoothie = True
else:
    milkshake = True
print("")

print("Summary of Drink:")
print("")
print("Fruit within the drink:")
print(fruit)
print("")
if fruit_juice == True:
    print("The drink should be a fruit juice.")
elif smoothie == True:
    print("The drink should be a smoothie.")
else:
    print("The drink should be a milkshake.")