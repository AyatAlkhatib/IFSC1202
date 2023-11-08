
# Step 1 - Create a class called "Student"
class Students ():
 # Step 2 - Define the initializer, the initializer should accept the folloing class values: 
  def __init__(self, firstname, lastname, tnumber, scores): 
     self.FirstName = firstname
     self.LastName = lastname
     self.TNumber = tnumber 
     self.Grade = scores
 # Step 4 - Define the methods for the object
  def RunningAverage(self): 
      total = 0 
      count = 0 
      for i in range (len(self.Grade)):
         if self.Grade[i].strip() != "": 
            total = total + float(self.Grade[i].strip())
            count = count + 1 
      return total / count  
  
  def TotalAverage(self): 
      total = 0 
      for i in range(len(self.Grade)):
         if self.Grade[i].strip() != "": 
          total = total + float(self.Grade[i].strip())
      return total / len(self.Grade)
  
  def LetterGrade(self): 
     Average = self.TotalAverage()
     if Average >= 90:
         return 'A'
     if Average >= 80: 
        return 'B'
     if Average >=70:
        return 'C'
     if Average >= 60:
        return 'D'
     
     return 'F'
    
# Read File 
StudentsFiles = open ("10.Project Student Scores.txt", "r")                  #We going to call the file as StudentFiles 
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("Name", "Name", "Number", "Average" ,"Average", "Grade"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("-"*12, "-"*12, "-"*12 ,"-"*12, "-"*12, "-"*12 ))
x= StudentsFiles.readline()   

# we want to print everything out now
while x != "": 
   y= x.split(",")
   Student = Students (y[0].strip(),y[1].strip(),y[2].strip(),y[3:])
   print("{:>12s} {:>12s} {:>12s} {:>12.2f} {:>12.2f} {:>12s}".format(Student.FirstName, Student.LastName, Student.TNumber, Student.RunningAverage(), Student.TotalAverage(), Student.LetterGrade()))
   x= StudentsFiles.readline()
