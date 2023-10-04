inputfile = open("06.Project Input File.txt", "r") 
outputfile = open("06.Project Output File.txt", "w") 
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
inputfile.close()
outputfile.close() 
print(inputrecords, "Input File Records")
print(outputrecords, "Output File Records")
print(mergerecords, "Merge File Records")





