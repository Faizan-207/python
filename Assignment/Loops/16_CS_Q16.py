num = int(input("Enter an integer: "))

sum_of_digits = 0

while num > 0:
    digit = num % 10  # Extract the last digit
    sum_of_digits += digit
    num //= 10  # Remove the last digit

print("Sum of digits:", sum_of_digits)
