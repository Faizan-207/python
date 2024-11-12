import time

desireTime = int(input("Enter your desire time in seconds:"))
seconds = 10
while desireTime > 0:
    print(desireTime)
    desireTime -= 1
    time.sleep(1)
