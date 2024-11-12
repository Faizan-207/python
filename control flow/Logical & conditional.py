eng_marks = int(input("Enter your english marks :"))
math_marks = int (input("Enter your math marks :"))

if eng_marks > 80 and math_marks > 80:
    print("'A' grade")
elif eng_marks > 80 or math_marks > 80:
    print("'B' grade")
else:
    print("'C' grade")