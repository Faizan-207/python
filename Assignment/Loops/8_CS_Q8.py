for number in range(10, 2, -1):
    flag = True
    for j in range(2, number):
        if number % j == 0:
            flag = False
            break
    if flag == True:
        print(number, end=" ")
