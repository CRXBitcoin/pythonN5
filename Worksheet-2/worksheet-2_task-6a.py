name = str(input("What is your name? "))
age = int(input("What is your age? "))

if age in range(4, 12):
    print(f"Hello {name}, you should be in primary school.")
elif age in range(12, 18):
    print(f"Hello {name}, you should be in high school.")
else:
    print(f"Hello {name}, you are not in the age range for this program.")