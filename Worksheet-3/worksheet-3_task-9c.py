print("Binary Converter v1.0.0")
print("Enter a decimal number to convert to binary:")
decimal_number = int(input())
binary_number = ""
if decimal_number == 0:
    binary_number = "0"
else:
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2

print("The binary representation is:", binary_number)