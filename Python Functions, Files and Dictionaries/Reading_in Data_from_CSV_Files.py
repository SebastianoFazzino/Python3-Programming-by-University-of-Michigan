#we can use open() to read simple .csv files

openfile = open('Olympics.txt', 'r')
lines = openfile.readlines()
for line in lines[:6]:
    print(line.strip())
    
print("\n_-_-_-_-_-_-_\n")


#using split(',') we split the values on comma

header = lines[0]
column_names = header.strip().split(',')
print(column_names)

for row in lines[1:]:
    values = row.strip().split(',')
    if values[5] != "NA":
        print("{}:{};{}".format(
            values[0],
            values[4],
            values[5]))
        