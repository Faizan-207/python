num = int(input("Enter an integer: "))
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10  # Remove the last
print(f"The reverse of given number is ", reverse_num)
