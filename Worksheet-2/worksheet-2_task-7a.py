percentage = float(input("What percentage did you get in the test? "))

if percentage >= 90:
    print("You got an A!")
elif percentage >= 70:
    print("You got a B!")
elif percentage >= 50:
    print("You got a C!")
elif percentage >= 40:
    print("You got a D!")
else:
    print("You did not pass.")