daily_temperatures = [10, 11, 12, 15, 17, 16, 18]
total = 0

for i in range(7):
    total = total + daily_temperatures[i]

average = total / 7
print(average, "degrees Celsius")