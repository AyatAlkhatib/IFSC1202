# create the array for property 
a= []

# Open the file and read the first line
csvfile = open("Exam Two Properties.csv")             # we going to name our file as csvfile 
x = csvfile.readline().strip()

# While not at the end of the file
while x != "":
    # Split the line into a list
    y = x.split(",")                                # this will make the lines to be slipted since we need lists 
    # we want the prices to be in floating number (the property is 4)
    y[4] = float(y[4])
    # Append the list to the two-dimensional array 
    a.append(y)
    # Read the next line
    x = csvfile.readline().strip()

csvfile.close()                              # after gathering the information we are going to close the file given to us

#creat a list for zipcodes
zipcodes = []

# Create an empty two dimensional list called "zipcodes". Each row in list will contain:
for property in a:                                       #Append the one dimensional list to a two dimensional list called "properties" that contains all of the data in
    zipcode_ = property[3]
    found = False
    for zipcode in zipcodes: 
         if zipcode_ == zipcode[0]:                 # Column 0 - Zip Code
            zipcode[1] += 1                          # Column 1 - Count of the number or properties with this zip code
            zipcode[2] += property[4]                #Column 2 - Sum of the price of the propeties in this zip code
            found = True
            break
    if not found: 
     zipcodes.append([zipcode_, 1, property[4]])           

print("Zipcode Count Average")


# Loop though each element in the list in the zipcode
for zipcode in zipcodes: 
      zipcode_ = zipcode[0]
      count = zipcode[1]
      average = zipcode[2] / count                          # The calcuation of Average Average Property Price - calculated as Sum of Prices (Column 2) divided by the Count of Properties (Column 1)
      # print the following information 
      print(f"{zipcode_}   {count}   ${average:.2f}")             





