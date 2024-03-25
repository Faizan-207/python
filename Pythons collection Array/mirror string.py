input_string = input("Enter string:")
n = int(input("Enter the value of n:"))

#Creating Dictionary
alphabets ="abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dictionary = dict(zip(alphabets,reverse_alphabets))

#Seperate the part of string to perform mirror operation
prefix = input_string[:n]
suffix = input_string[n:]

#Finding mirror string
mirror =""
for i in range(len(suffix)):
    mirror+= dictionary[suffix[i]]

#Result string
print("Result is :",prefix +  mirror)



