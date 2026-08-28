print("Q1: What is the capital of France?")
print("A. Paris")
print("B. London")
print("C. Berlin")
print("D. Madrid")

answer = input("Enter your answer (A, B, C, or D): ")
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Invalid input. Please enter a valid answer (A, B, C, or D).")
    answer = input("Enter your answer (A, B, C, or D): ")

if answer == "A":
    print("Correct! The capital of France is Paris.")
else:
    print("Incorrect. The capital of France is Paris.")