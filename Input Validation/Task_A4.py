previous_meter_reading = float(input("Enter the previous meter reading: "))
current_meter_reading = float(input("Enter the current meter reading: "))
while current_meter_reading < previous_meter_reading:
    print("Invalid meter reading. Please enter a number greater than or equal to the previous reading.")
    current_meter_reading = float(input("Enter the current meter reading: "))

unit_cost = float(input("Enter the cost per unit (pence): "))
while unit_cost < 0:
    print("Invalid unit cost. Please enter a number greater than or equal to 0.")
    unit_cost = float(input("Enter the cost per unit (pence): "))

discount_eligible = str(input("Are you eligible for a £5 discount? (Y/N): "))
discount_eligible = discount_eligible.upper()
while discount_eligible != "Y" and discount_eligible != "N":
    print("Invalid input. Please enter Y or N.")
    discount_eligible = str(input("Are you eligible for a £5 discount? (Y/N): "))

units_used = current_meter_reading - previous_meter_reading
total_cost = units_used * unit_cost
if discount_eligible == "Y":
    total_cost -= 5

print("Electricty Cost")
print("Units Used: ", units_used)
print(units_used, "units at", unit_cost, "pence per unit")
total_cost = total_cost / 100
print("= £", total_cost)
total_cost = round(total_cost, 2)
print("")
print("Final bill: £", total_cost)