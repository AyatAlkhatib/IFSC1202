# a file containing angles in degrees, minutes, seconds format (DD°MM'SS"), converts the value to a decimal degree value, then write the values to a file. 
# DD stands for degrees 
# MM stands for minutes 
# SS stands for seconds 

def parseDegreeString (ddmmss):
    degree_symbol = (chr(176))                        # represent the symbol that was used for the degree 
    minutes_symbol = ("'")
    seconds_symbol = ('"')
# the positions of the symbols
    Degree_position= ddmmss.find(degree_symbol)
    minutes_position = ddmmss.find(minutes_symbol)
    Seconds_position = ddmmss.find(seconds_symbol)
# floating points for the degrees, minutes, and seconds
    Degrees= float(ddmmss[0:Degree_position])
    Minutes = float (ddmmss [Degree_position+1:minutes_position])
    Seconds= float(ddmmss[minutes_position+1:Seconds_position])
    return Degrees, Minutes, Seconds

def DDMMSStoDecimal (Degrees, Minutes, Seconds):
    # we want to convert each one to a decimal 
    Degree_Decimal = Degrees + (Minutes/60.0) + (Seconds/3600.0)
    return Degree_Decimal


#read the inputfile and write outputfile 
inputfile = open("07.Project Angles Input.txt", "r")
outputile = open ("07.Project Angles Output.txt", "w")
records_processed = 0                                        #the starting records for the file will be 0 

for line in inputfile:
    line = line.strip()                                               # represents the lines in the inputfile 
    if line: 
        Degrees, Minutes, Seconds = parseDegreeString (line)
        Degree_Decimal= DDMMSStoDecimal (Degrees, Minutes, Seconds)
        outputile.write(str(Degree_Decimal) + "\n")                        #\n is because we want a newline 
        records_processed +=1                                               
   
inputfile.close()
outputile.close()
print(records_processed, "Records Processed") 



    

