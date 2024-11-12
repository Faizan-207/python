a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a + b > c and b + c > a and c + a > b:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")
