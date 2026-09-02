test_score = [0]
test_Score = int(input("Enter the test score: "))
while test_Score < 0 or test_Score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    test_Score = int(input("Enter the test score: "))
test_score[0] = test_Score