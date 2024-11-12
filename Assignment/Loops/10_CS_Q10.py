num = int(input("Enter an integer: "))

count = 0
while num > 0:
    count += 1
    num //= 10  # Remove the last digit

print("The number of digits is:", count)
