print("Average Score Calculator v1.0.0")
maths_score = int(input("What is your score in Maths? (percentage) "))
english_score = int(input("What is your score in English? (percentage) "))
computing_score = int(input("What is your score in Computing? (percentage) "))
average_score = (maths_score + english_score + computing_score) / 3
print("Your average score is " + str(average_score) + "%.")