# Speed Calculator v1.0.0 
print("Speed Calculator v1.0.0")
print("What is the distance travelled (in metres)?")
distance = int(input())
print("What is the time taken (in seconds)?")
time = int(input())
speed = distance / time
rounded_speed = round(speed, 2)
print("The speed of the object is ", rounded_speed," metres per second.")

# Average Score Calculator v1.0.0
print("Average Score Calculator v1.0.0")
maths_score = int(input("What is your score in Maths? (percentage) "))
english_score = int(input("What is your score in English? (percentage) "))
computing_score = int(input("What is your score in Computing? (percentage) "))
average_score = (maths_score + english_score + computing_score) / 3
rounded_average = round(average_score, 2)
print("Your average score is " + str(rounded_average) + "%.")

# Percentage Calculator v1.0.0
print("Percentage Calculator v1.0.0")
original_price = int(input("What is the original price of the item? (in pounds) "))
discount = original_price * 0.20
final_price = original_price - discount
rounded_final_price = round(final_price, 2)
print("The final price of the item after the discount is ", rounded_final_price, " pounds.")

# Weight Calculator v1.0.0
print("Weight Calculator v1.0.0")
mass = int(input("What is the mass of the object? (in kilograms) "))
earth_gravity = 9.81
weight = mass * earth_gravity
rounded_weight = round(weight, 2)
print("The weight of the object on Earth is ", rounded_weight," Newtons.")
