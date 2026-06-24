print("What is your name?")
name = str(input())
print("How many times would you like your name to be displayed?")
loopNo = int(input())
for counter in range(0, loopNo):
    print(name)