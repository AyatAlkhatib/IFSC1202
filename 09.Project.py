# Create the array
a = []
# Open the file and read the first line
csvFile = open("09.Project Distances.csv")
x = csvFile.readline().strip()
# While not at end of file 
while x != "":
# Split the line into a list
	y = x.split(",")
# Convert the values from string to an integer
#	for i in range(len(y)):
#		y[i] = int(y[i])
# Append the list to the two dimensional array
	a.append(y)
# Read the next line
	x = csvFile.readline().strip()
# Loop through each row in the two dimensional array
for i in range(len(a)):
# Loop though each element in the list
    for j in range(len(a[i])):
# Print each element in the list
        print(
              '{:>10}'.format(a[i][j]), end=' ')
# End of list - go to next line
    print() 



from_city = input("From City: ")
to_city= input("To City: ")
from_city_row = 0 
to_city_row = 0 


for i in range(len(a)): 
      if a[i][0] == from_city:
            from_city_row = i 
            break 
for i in range (len(a[0])):
      if a[0][i] == to_city: 
            to_city_colum = i 
            break 

for i in range(len(a)):
      if from_city_row == 0:
            print("Invalid to City")
            break 
for i in range(len(a[0])):
      if to_city_colum == 0: 
            print("Invalid to City")
            break 
#print 
print(f"{from_city} to {to_city} - {a[from_city_row][to_city_colum]} Miles")
