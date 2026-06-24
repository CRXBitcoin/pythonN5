pass_1 = str(input("Enter the Password:"))
pass_2 = str(input("Re-enter the Password:"))
pass_3 = str(input("Re-enter the Password again:"))

if pass_1 == pass_2 == pass_3:
    print("Access granted. Welcome to the system!")
else:
    print("Passwords do not match. Access denied. Please try again.")