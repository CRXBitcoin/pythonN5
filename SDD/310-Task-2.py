test_scores = []
total = 0
for counter in range(0, 5):
    test_scores.append(int(input("Enter the test score for test " + str(counter + 1) + ": ")))
    total += test_scores[counter]
    print("Total score so far: ", total)
print("")
print("Total score for all tests: ", total)