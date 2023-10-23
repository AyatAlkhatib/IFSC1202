import csv

# read the input distance provided in the cvs.file 
with open("09.Project Distances.csv", newline='') as distancecsv: 
    distance_information = list(csv.reader(distancecsv))

# display the cvs file table into rows 
for row in distance_information:
    print("\t".join(row))

#Prompt for a From City
from_city = input("Enter from city: ").strip()

#Prompt to a city 
to_city = input("Enter To City: ").strip()

#where is the index of the column where the city 
index_from_city = None
for i, row in enumerate (distance_information): 
    if from_city == row [0]: 
        index_from_city = i 
        break

# find the index of the row 
index_to_city = None
if index_to_city is not None: 
    for i, city in enumerate (distance_information[0]): 
        if to_city == city: 
            index_to_city = i 
            break 

# If the From City was not found
if index_from_city is None: 
    print("Invalid From City")
if index_to_city is None: 
    print("Invalid To City")

#If both cities where found 
if index_from_city is not None and index_to_city is not None:
    distance = distance_information[index_from_city][index_to_city]
    print(f"{from_city} to {to_city} - {distance} Miles")


