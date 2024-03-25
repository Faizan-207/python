numbers = [2,2,4,5,6,7,4,3,8,7,5,3,2,6]
new_num =[]
for i in numbers:
    if i not in new_num:
        new_num.append(i)
print(new_num)