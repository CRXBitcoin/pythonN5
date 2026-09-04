home = 0
away = 0
period = 1
print("Welcome to the hockey game scoreboard!")
print("")
print("Would you like to begin the game? (Y/N)")
begin_game = input().upper()
if begin_game == "Y":
    print("Game has begun!")
    print("")
    print("Period: ", period)
    print("Home: ", home, " Away: ", away)
    print("")
    print("Press 'h' to add a goal for the home team, 'a' to add a goal for the away team, or 'x' to end the current period.")
    input_char = input().lower()
    while input_char != "x" or period <= 3:
        if input_char == "h":
            home += 1
            print("Goal for the home team!")
        elif input_char == "a":
            away += 1
            print("Goal for the away team!")
        elif input_char == "x":
            if period < 3:
                period += 1
                print("Period ended. Moving to the next period.")
            else:
                print("Game over!")
                print("Final Score: Home: ", home, " Away: ", away)
        else:
            print("Invalid input. Please try again.")
        print("")
        print("Period: ", period)
        print("Home: ", home, " Away: ", away)
        print("")
        print("Press 'h' to add a goal for the home team, 'a' to add a goal for the away team, or 'x' to end the current period.")
        input_char = input().lower()
else:
    print("Exiting the program...")