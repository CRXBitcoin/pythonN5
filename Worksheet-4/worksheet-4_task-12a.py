print("10-Questions.com v1.0.0")
print("All answers should be capitalised with spaces between words, if necessary.")

print("Q1: What is the capital of France?")
q1_answer = input()
if q1_answer == "PARIS":
    print("Correct!")
else:
    print("Incorrect!")

print("Q2: What is the largest planet in our solar system?")
q2_answer = input()
if q2_answer == "JUPITER":
    print("Correct!")
else:
    print("Incorrect!")

print("Q3: What is the chemical symbol for water?")
q3_answer = input()
if q3_answer == "H2O":
    print("Correct!")
else:
    print("Incorrect!")

print("Q4: Who wrote the play 'Romeo and Juliet'? (First and last name)")
q4_answer = input()
if q4_answer == "WILLIAM SHAKESPEARE":
    print("Correct!")
else:
    print("Incorrect!")

print("Q5: What is the capital of Japan?")
q5_answer = input()
if q5_answer == "TOKYO":
    print("Correct!")
else:
    print("Incorrect!")

print("Q6: What is the largest mammal in the world?")
q6_answer = input()
if q6_answer == "BLUE WHALE":
    print("Correct!")
else:
    print("Incorrect!")

print("Q7: What is the chemical symbol for gold?")
q7_answer = input()
if q7_answer == "AU":
    print("Correct!")
else:
    print("Incorrect!")

print("Q8: Who painted the Mona Lisa? (First and last name)")
q8_answer = input()
if q8_answer == "LEONARDO DA VINCI":
    print("Correct!")
else:
    print("Incorrect!")

print("Q9: What is the capital of Australia?")
q9_answer = input()
if q9_answer == "CANBERRA":
    print("Correct!")
else:
    print("Incorrect!")             

print("Q10: What is the smallest prime number?")
q10_answer = input()
if q10_answer == "2":
    print("Correct!")
else:
    print("Incorrect!")

final_score = 0
if q1_answer == "PARIS":
    final_score += 1
if q2_answer == "JUPITER":
    final_score += 1
if q3_answer == "H2O":
    final_score += 1
if q4_answer == "WILLIAM SHAKESPEARE":
    final_score += 1
if q5_answer == "TOKYO":
    final_score += 1
if q6_answer == "BLUE WHALE":
    final_score += 1
if q7_answer == "AU":
    final_score += 1
if q8_answer == "LEONARDO DA VINCI":
    final_score += 1
if q9_answer == "CANBERRA":
    final_score += 1
if q10_answer == "2":
    final_score += 1

print(f"Your final score is: {final_score}/10")