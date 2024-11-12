height = int(input("enter the height of triangle"))
char = 'A'
for i in range(1,height+1):
    j = 1
    while j<=i:
      print(char,end="")
      j+= 1
      char = chr(ord(char) + 1)
    print()