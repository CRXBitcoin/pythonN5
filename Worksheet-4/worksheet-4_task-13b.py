Student = [] 
Score = [] 
for counter in range (0,5):
    print("Enter your name:")
    name = str(input())
    print("Enter your score: (out of 150)")
    score = int(input())
    while score <0 or score >150:
        print("Invalid score. Please enter a score between 0 and 150:")
        score = int(input())
    Student.append(name)
    Score.append(score)

print("Results:")
for counter in range (0,5):
    if Score[counter] >= 105:
        print("Passed:")
        print(Student[counter], "with a score of", Score[counter])
    else:
        print("Failed:")
        print(Student[counter], "with a score of", Score[counter], "did not pass.")
