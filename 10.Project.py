
# Step 1 - Create a class called "Student"
class Students ():
 # Step 2 - Define the initializer, the initializer should accept the folloing class values: 
  def __init__(self, firstname, lastname, tnumber, scores): 
     self.FirstName = firstname
     self.LastName = lastname
     self.TNumber = tnumber 
     self.Grade = [int(score) if score.strip() else 0 for score in scores]
 # Step 4 - Define the methods for the object
  def RunningAverage(self): 
    RunningAverage = [grade for grade in self.Grades if grade != 0]
    if RunningAverage: 
        return sum(RunningAverage)/len(RunningAverage) 
    else: 
        return 0 
  def TotalAverage(self): 
    return sum(self.Grade) / len(self.Grade)
  
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
    
# Step 5 -  Create list
student = []


# Read File 
StudentsFiles = open ("10.Project Student Scores.tx")
for line in StudentsFiles:
        x = StudentsFiles.readline().strip()
        data = line.strip().split(",")
        firstname, lastname, tnumber, *scores = data
        students= x(firstname, lastname, tnumber, scores(0))
        Students.append(student)

# Print the header
print(f"{'First Name':<12}{'Last Name':<12}{'ID':<12}{'Running':<12}{'Semester':<12}{'Letter':<12}")
print(f"{'':<12}{'':<12}{'Number':<12}{'Average':<12}{'Average':<12}{'Grade':<12}")
print("-" * 72)

# Print student data
for students in student:
    running_avg = student.RunningAverage()
    semester_avg = student.TotalAverage()
    letter_grade = student.LetterGrade()
    print(f"{student.FirstName} {student.LastName} {student.TNumber} {running_avg:} {semester_avg:} {letter_grade}")

