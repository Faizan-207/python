temperature = float(input("Enter the temperature in Celsius: "))

if temperature <= 0:
    print("It's freezing!")
elif temperature <= 25:
    print("The temperature is moderate.")
else:
    print("It's hot!")num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
else:
    print("Invalid operator")

if operator in '+-*/':
    print(f"{num1} {operator} {num2} = {result}")
