# Open Input File for Reading
inputfile = open("06.Project Input File.txt", "r") 
# Open Output File for Writing
outputfile = open("06.Project Output File.txt", "w") 
# File Records
inputrecords = 0
outputrecords= 0 
mergerecords = 0 
line= inputfile.readline()
while line !="":
    if line == "**Insert Merge File Here**":
        mergefilename = open ("06.Project Merge File.txt", "r")
        mergefile= mergefilename.readline()
        while mergefile !="":
           outputfile.write(mergefile)  
        outputrecords +=1 
        mergefilename.close()
    else: 
       outputfile.write(line)
       outputrecords +=1 
       inputrecords +=1
    line = inputfile.readline()
# Close all the Files
inputfile.close()
outputfile.close() 
# Print the records of the Files
print(inputrecords, "Input File Records")
print(outputrecords, "Output File Records")
print(mergerecords, "Merge File Records")





