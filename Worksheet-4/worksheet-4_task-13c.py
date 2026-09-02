print("10-Questions.com v1.0.0")
print("All answers should be capitalised with spaces between words, if necessary.")

Question = ["What is the capital of France?","What is the largest planet in our solar system?","What is the chemical symbol for water?"]
Answer = ["PARIS", "JUPITER", "H2O"]
score = 0

for counter in range(0,3):
    print(Question[counter])
    user_answer = input().upper()
    if user_answer == Answer[counter]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print(f"Your final score is: {score}/3")