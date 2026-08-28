# PROJECT

import random

words = ["python", "function", "random", "length", "computer", "program", "variable"]

secret_word = random.choice(words)
counter = 1
score = 0
while counter in range(1,6):
    guess = input("Guess the secret word: ")
    if guess == secret_word:
        print("Correct!")
        score = len(secret_word) / counter
        rounded_score = round(score, 1)
        print("Your score is:", rounded_score)
    else:
        print("Incorrect!")
        counter += 1
        if counter == 6:
            print("Sorry, you have used all your attempts. The secret word was:", secret_word)
            rounded_score = 0
print("Your final score is:", rounded_score)