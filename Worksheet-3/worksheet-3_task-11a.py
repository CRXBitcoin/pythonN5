valid == False
while valid == False:
    print("What age are you?")
    age=int(input())
    if age < 0 or age > 120:
        print("Age Invalid.")
        print("Please enter an age between 0 and 120.")
    else:
        valid == True
        print("Input is Valid.")