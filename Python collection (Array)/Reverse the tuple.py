#Reverse the tuple
tupe= (3,5,6,2,7)
list = []
for i in reversed(tupe):
    list.append(i)
print(tuple(list))

# WHY TUPLE?
# We can itrate fastly through tuple than list.
# Tuple are immutable elements so these can be used a krys in dictionaries