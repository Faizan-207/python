dic = {
    "a": 123, "b": 456, "c": 789
}
#print(dic["a"])

#Adding dictionary
new_dic = {"d":222}
dic.update(new_dic)
print(dic)

#Removing a element from dictionary
dic.pop("d")
print(dic)

dic.popitem() # Remove from the last
print(dic)

# Empty th dictionary
new_dic.clear()
print(new_dic)

#Printing elements of dictionary
for i,j in dic.items():
    print(i,j)

#Nested Dictionary
dictionary = {
    "value1":{
        "a":1,
        "b":2,  
        "c":3},

     "Value2":{
        "d":4,
        "e":5,
        "f":6
    }}
print(dic.keys())
   
