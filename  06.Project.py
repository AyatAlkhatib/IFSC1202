# The name of the file can be a string
inputfilename = "06.Project Input File.txt"
outputfilename ="06.Project Output File.txt"
# Open the input file for reading
inputfile = open("06.Project Input File.txt", "r") 
# Open the output file for writing
outputfile = open("06.Project Output File.txt", "w") 
#file records
inputrecords = 0
outputrecords= 0 
mergerecords = 0 
for line in inputfile:
    inputrecords +=1
    if "**Insert Merge File Here**":
        mergefile = open ("06.Project Merge File.txt")
        for line in mergefile: 
            mergerecords +=1 
            for line in outputfile: 
                if "**Insert Merge File Here**": 
                    outputrecords +=1 
inputfile.close 
outputfile.close

print ({inputrecords}, inputfile)
print({mergerecords}, mergefile)
print ({outputrecords}, outputfile)




