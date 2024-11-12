fruits = ["Apple","Banana","Kiwi","Papya"]
print(fruits)
new = ["Mangos","Oranges","Graps"]

#Acessing of elemnts at different indexs
print(fruits[2])
print(fruits[:2])

#Adding element in list
fruits.append("Pomigrant")
print(fruits)

#Adding at specific index
fruits.insert(2,"Straberry")
print(fruits)

#Add a whole exsiting list
fruits.extend(new)
print(fruits)
print(len(fruits))

#removing a element 
fruits.remove("Banana")#Method 1
fruits.pop()# Method 2
print(fruits)

#Updating a item or a list of items
fruits[-1]="Graps"
print(fruits)

#Sorting of list
fruits.sort() # Default acending
print(fruits)
fruits.sort(reverse=True) #decendinf order
print(fruits)
fruits.reverse() #reverse the list
print(fruits)

#list comprehension
new_fruits = [i for i in fruits if "r" in i ]
print(new_fruits)

# Copy of list
new_f = fruits
print(new_f)

#List Concatination
new_f += fruits
print(new_f)

#Nested list
print(new_fruits)
new_fruits.insert(2,["PineApple","kishmish"])
print(new_fruits)
print(new_fruits[2][1])

#Triverse the elements of List
for i in new_fruits:
    print(i)