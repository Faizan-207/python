number = int(input("Enter a number: "))
lower_limit = int(input("Enter the lower limit of the range: "))
upper_limit = int(input("Enter the upper limit of the range: "))

if number >= lower_limit and number <= upper_limit:
    print(number, "is within the range", lower_limit, "to", upper_limit)
else:
    print(number, "is not within the range", lower_limit, "to", upper_limit)
