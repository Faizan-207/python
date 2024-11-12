number = int(input("Enter a number of terms to find :"))
a = 0
b = 1
print(a, end=" ")
for i in range(1, number):
    next = a + b
    a = b
    b = next
    print(next, end=" ")
