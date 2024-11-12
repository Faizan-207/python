n = int(input("Enter the length of list:"))
list = []
for i in range (n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter index 1:"))
idx2 = int(input("Enter index 2:"))
#Before swaping 
print(list)

#After swaping
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print(list)
