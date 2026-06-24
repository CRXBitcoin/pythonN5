print("Calorie Calculator")
total_calories = 0
for index in range (1, 6):
    print("How many calories did you consume today?")
    calories = int(input())
    total_calories += calories
    calories = 0
print("Total calories consumed today:", total_calories)