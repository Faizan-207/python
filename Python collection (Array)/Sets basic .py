set1 = {"we","you","he","she"}
# Adding elements in sets
set1.add("it")
print(set1)

# Cobine another set
set2 = {"They","my"}
set1.update(set2)
print(set1)

#Remove an element from set
set1.remove("it")
print(set1) 
set1.discard("they")

