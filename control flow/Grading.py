marks = int(input("Enter your marks percentage: "))
if marks >= 80:
    grade = 'A'
elif marks >=60:
    grade = 'B'
elif marks >=50:
    grade = 'C'
elif marks >=20:
    grade ='D'
else:
    grade = 'F'
print ("Your grade is ",grade)

