a,b,c = map(int,input("Enter 3 numbers seperaterd by sapce :").split())
if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c
print("Greatest number is ",max)  



#2nd method
#By logical operator
"""
a,b,c = map(int,input("Enter 3 numbers seperaterd by sapce :").split())
if a > b and a > c:
    max = a
elif b > a and b > c :
    max = b
else:
    max = c
print("Greatest number is ",max)         

"""