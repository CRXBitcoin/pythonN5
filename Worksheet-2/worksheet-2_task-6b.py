test_1_result = int(input("What was your result for test 1 out of 100? "))
test_2_result = int(input("What was your result for test 2 out of 100? "))

if test_1_result > 60 and test_2_result > 50:
    print("You are eligible to sit test 3.")
else: 
    print("You are not eligible to sit test 3. You needed to score above 60% in test 1 and above 50% in test 2.")