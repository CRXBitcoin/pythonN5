for counter in range(1, 11):
    test_score = float(input("What was your test score out of 70? "))
    test_percentage = (test_score / 70) * 100
    if test_percentage > 70:
        print("You passed the test!")
    else:
        print("You failed the test. You needed to score above 70% to pass.")