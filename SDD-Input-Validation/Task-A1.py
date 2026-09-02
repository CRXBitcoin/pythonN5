test_score = [""]
test_score = int(input("Please enter your test score (0-100): "))
while test_score < 0 or test_score > 100:
    print("Invalid input. Please enter a score between 0 and 100.")
    test_score = int(input("Please enter your test score (0-100): "))
