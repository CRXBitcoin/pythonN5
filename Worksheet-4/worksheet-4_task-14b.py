firstname = input("Please enter your first name: ")
secondname = input("Please enter your last name: ")
yearofbirth = int(input("Please enter your year of birth: "))

print("Suggested username: " + firstname[0] + secondname + str(yearofbirth)[2:4])