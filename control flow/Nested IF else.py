salary = int(input("Enter your salray"))
if salary >= 20000:
    net = salary - (salary * 0.07) # Deduct 7% of  orignal salary
elif salary >=10000:
    net = salary - (salary * 0.02)# Deduct 2% of orignal salray
else:
    net = salary
print("Your net salary is :",net)