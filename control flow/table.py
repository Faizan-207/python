table_no = int(input("Table number :"))
starting = int(input("Starting point :"))
ending = int(input("Ending point :"))
for starting in range(starting,ending+1):
    print(table_no,"*",starting,"=",starting * table_no)