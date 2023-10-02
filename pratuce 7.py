# The name of the file can be a string
inputfilename = "06.Project Input File.txt"
outputfilename = "06.Project Output File.txt"
mergefilename = "06.Project Merge File.txt"

# Open the input file for reading
inputfile = open(inputfilename, "r")

# Open the output file for writing
outputfile = open(outputfilename, "w")

# Initialize record counters
inputrecords = 0
mergerecords = 0
outputrecords = 0

# Read data from the input file
for line in inputfile:
    inputrecords += 1
    # You need to specify a condition to determine when to merge data
    # For example, if you want to merge when a specific text is found in the line:
    if "**Insert Merge File Here**" in line:
        # Open and read the merge file
        mergefile = open(mergefilename, "r")
        for merge_line in mergefile:
            mergerecords += 1
            # You can process the data from the merge file here and write it to the output file
            # For now, let's just write it as-is
            outputfile.write(merge_line)
        mergefile.close()
    else:
        # If no merge condition is met, write the input line to the output file
        outputfile.write(line)
        outputrecords += 1

# Close the input and output files
inputfile.close()
outputfile.close()

# Print the record counts
print("Input Records:", inputrecords)
print("Merge Records:", mergerecords)
print("Output Records:", outputrecords)
