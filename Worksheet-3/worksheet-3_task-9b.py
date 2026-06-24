print("Hi-Lo v1.1.0")
import random
number = random.randint(1, 100)
guess = 0
attempts = 0
while guess != number:
    print("Guess a number between 1 and 100:")
    guess = int(input())
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        print("It took you", attempts, "attempts to guess the number.")