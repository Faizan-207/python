for number in range(2, 50):
    flag = True
    for j in range(2, number):
        if number % j == 0:
            flag = False
            break
    if flag == True:
        print(number, end=" ")
