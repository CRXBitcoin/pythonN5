print("10-Questions.com v1.0.0")
print("All answers should be fully capitalised with spaces between words, if necessary.")

q1_answer = ""
q2_answer = ""
q3_answer = ""
q4_answer = "" 
q5_answer = ""
q6_answer = ""
q7_answer = ""
q8_answer = ""
q9_answer = ""
q10_answer = ""

q1_attempts = q2_attempts = q3_attempts = q4_attempts = q5_attempts = 0
q6_attempts = q7_attempts = q8_attempts = q9_attempts = q10_attempts = 0

while q1_answer != "PARIS":
    print("Q1: What is the capital of France?")
    q1_answer = input()
    q1_attempts += 1
    if q1_answer == "PARIS":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q2_answer != "JUPITER":
    print("Q2: What is the largest planet in our solar system?")
    q2_answer = input()
    q2_attempts += 1
    if q2_answer == "JUPITER":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q3_answer != "H2O":
    print("Q3: What is the chemical symbol for water?")
    q3_answer = input()
    q3_attempts += 1
    if q3_answer == "H2O":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q4_answer != "WILLIAM SHAKESPEARE":
    print("Q4: Who wrote the play 'Romeo and Juliet'? (First and last name)")
    q4_answer = input()
    q4_attempts += 1
    if q4_answer == "WILLIAM SHAKESPEARE":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q5_answer != "TOKYO":
    print("Q5: What is the capital of Japan?")
    q5_answer = input()
    q5_attempts += 1
    if q5_answer == "TOKYO":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q6_answer != "BLUE WHALE":
    print("Q6: What is the largest mammal in the world?")
    q6_answer = input()
    q6_attempts += 1
    if q6_answer == "BLUE WHALE":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q7_answer != "AU":
    print("Q7: What is the chemical symbol for gold?")
    q7_answer = input()
    q7_attempts += 1
    if q7_answer == "AU":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q8_answer != "LEONARDO DA VINCI":
    print("Q8: Who painted the Mona Lisa? (First and last name)")
    q8_answer = input()
    q8_attempts += 1
    if q8_answer == "LEONARDO DA VINCI":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q9_answer != "CANBERRA":
    print("Q9: What is the capital of Australia?")
    q9_answer = input()
    q9_attempts += 1
    if q9_answer == "CANBERRA":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

while q10_answer != "2":
    print("Q10: What is the smallest prime number?")
    q10_answer = input()
    q10_attempts += 1
    if q10_answer == "2":
        print("Correct!")
    else:
        print("Incorrect! Please try again.")

print("Thank you for playing 10-Questions.com v1.0.0! You have answered all the questions!")
print("Attempt summary:")
print(f"Q1: {q1_attempts}  Q2: {q2_attempts}  Q3: {q3_attempts}  Q4: {q4_attempts}  Q5: {q5_attempts}")
print(f"Q6: {q6_attempts}  Q7: {q7_attempts}  Q8: {q8_attempts}  Q9: {q9_attempts}  Q10: {q10_attempts}")