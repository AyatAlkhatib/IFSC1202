
# Step 1 - Create a class called "Student"
class Students ():
 # Step 2 - Define the initializer, the initializer should accept the folloing class values: 
  def __init__(self, firstname, lastname, tnumber, scores): 
     self.FirstName = firstname
     self.LastName = lastname
     self.TNumber = tnumber 
     self.Grades = [int(score) if score.strip() else 0 for score in scores]
 # Step 4 - Define the methods for the object
  def RunningAverage(self): 
    RunningAverage = [scores for scores in self.Grades if scores != 0]
    if RunningAverage: 
        return sum(RunningAverage)/len(RunningAverage)
    else: 
        return 0 
  def TotalAverage(self): 
    return sum(self.Grades) / len(self.Grades)
  
  def LetterGrade(self): 
     Average = self.TotalAverage()
     if Average >= 90:
         return 'A'
     if 80 <= Average < 90: 
        return 'B'
     if 70 <= Average < 80:
        return 'C'
     if 60 <= Average < 70:
        return 'D'
     if Average < 60: 
        return 'f'
    
# Step 5 -  Create 4 instances of students
mystudent1 = Students("Jim","Evans","T123456", [95, 0, 71])
mystudent2 = Students("Joe","Smith","T654321", [90, 80, 85, 97])
mystudent3 = Students("Jane","Doe", "T121212",[0, 100, 99])

# create array 
Students = [mystudent1, mystudent2, mystudent3]

# Read File 
StudentsFiles = open ("10.Project Student Scores.tx")
for line in StudentsFiles:
        data = line.strip().split(",")
        firstname, lastname, tnumber, *scores = data
        student = Students(firstname, lastname, tnumber, scores(0))
        Students.append(student)

#Print the attributes
for student in Students: 
    print(f"{student.FirstName} {student.LastName}'s Running Average: {student.RunningAverage()}")
    print(f"{student.FirstName} {student.LastName}'s Total Average: {student.TotalAverage()}")
    print(f"{student.FirstName} {student.LastName}'s Letter Grade: {student.LetterGrade()}")


