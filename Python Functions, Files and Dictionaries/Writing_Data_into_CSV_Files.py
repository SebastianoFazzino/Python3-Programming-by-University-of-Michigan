olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")

outfile.write("Name, Age, Sport")
outfile.write("\n")


#we iterate through 'olympians' list to write data into 'reduced_olympics.csv'

for olympian in olympians:
    rows = "{},{},{}".format(
        olympian[0],
        olympian[1],
        olympian[2])
    outfile.write(rows)
    outfile.write("\n")

outfile.close()




#this is another way for writing data into a csv file using a join operator:
  
outfile2 = open("reduced_olympics2.csv", "w")

outfile2.write("Name, Age, Sport")
outfile2.write("\n")

for olympian in olympians:
    rows = ",".join([olympian[0],str(olympian[1]),olympian[2]])
    outfile2.write(rows)
    outfile2.write("\n")
    
outfile2.close()
    




#a third option for writing data into a csv file is using strings concatenation:
    
outfile3 = open("reduced_olympics3.csv", "w")

outfile3.write("Name, Age, Sport")
outfile3.write("\n")   

for olympian in olympians:
    rows = olympian[0] + "," + str(olympian[1]) + "," + olympian[2]
    outfile3.write(rows)
    outfile3.write("\n")
    
outfile3.close()

