num1 = int(input("Enter firsst number :"))
num2 = int (input("Enter second number :"))
operator = input("Operation to perform(+, -, *, /, %)")

match operator:
    case'+':
        print("Sum is :",num1 + num2)
    case'-':
        print("Difference is :",num1 - num2)    
    case'*':
        print("Multiplication is :", num1 * num2 )
    case'/':
        print("Division is :",num1 / num2)
    case'%':
        print ("Reminder is :",num1 % num2)
    