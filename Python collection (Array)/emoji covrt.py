string = input(">")
words = string.split(" ")
dict = { ":(": "😟",  ":)":"🙂" }
output = ""
for i in words:
    output+= dict.get(i,i) + " "
print(output)