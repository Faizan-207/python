year = int(input("Enter a year: "))

if year % 100 == 0:
    print(year, "is a century year.")
else:
    print(year, "is not a century year.")