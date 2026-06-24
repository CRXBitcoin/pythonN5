english = str(input("Do you take English? (True/False) "))
drama = str(input("Do you take Drama? (True/False) "))
music = str(input("Do you take Music? (True/False) "))
count = 0

if english == "True":
    count = count + 1
if drama == "True":
    count = count + 1
if music == "True":
    count = count + 1

if count >= 2:
    print("You are eligible to attend the London trip.")
else:
    print("You are not eligible to attend the London trip. You needed to take at least 2 of the subjects: English, Drama, Music.")