# Step 1 - Create a class called "Student"
Class Students(): 

# Step 2 - Define the initializer, the initializer should accept the folloing class values
def __init__(firstname, lastname, tnumber, scores): 

# Step 3 - In the initializer, create the following object attributes
self.FirstName = firstname
self.LastName = lastname
self.TNumber = tnumber 
self.Grades = [int(scores) for score in scores] 

# Step 4 - Define the methods for the object
def RunningAverage(self): 
    RunningAverage = [scores for scores in self.Grades if scores != 0]
    if RunningAverage: 
        return sum(RunningAverage)/len(RunningAverage)
    else: 
        return 0 


def TotalAverage(self): 




