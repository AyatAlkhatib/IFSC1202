
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
  
# Step 1: Define the class object "StudentList"
  class StudentList(): 
   # Step 2: Define the initializer and any default values
   def __init__(self): 
      # Step 3: Define the object attributes
      self.StudentList = []
   # Step 4 - Define the methods for the object
   def add_student(self,FirstName, LastName, TNumber): 
      # Create A new Student object 
      mystudent = Students(FirstName, LastName, TNumber,)
      # Append Student object to list
      self.StudentList.append(mystudent)

    # find student 
      index = self.find_student(TNumber) 

   #print_student_list 
   def print_ball_list(self):
    print("{:>14s}{:>14s}{:>14s}{:>14s}".format("Type", "FirstName", "LastName", "TNumber"))
    for i in range(len(self.StudentList)):
        print ("{:>14s}{:14.2f}{:14.2f}{:14.2f}".format(self.StudentList[i].FirstName, self.StudentList[i].LastName, self.StudentList[i].TNumber()))
        print()
        print("{} Students in list".format(self.number_of_Students()))
        print()
      
# Read File 
studentfiles = open("11.Project Students.txt" , "r")
def add_student_from_file(self, studentfiles):
		x = studentfiles.readline()
		while x != "":
#			print(x) # display what was read
			y = x.split(",")
#			print(y) # display the result of the split
			self.add_student(y[0].strip(), float(y[1].strip()), float(y[2].strip()))
			x = studentfiles.readline()
		studentfiles.close()
        
#-------------------------------------------------------------------- 

# Create a student List
mystudentlist = open("11.Project Scores.txt")

# Read scores List from File
mystudentlist.add_scores_from_file("11.Project Scores.txt")
def add_scores_from_file(self, mystudentlist):
		x = mystudentlist.readline()
		while x != "":
#			print(x) # display what was read
			y = x.split(",")
#			print(y) # display the result of the split
			self.add_student(y[0].strip(), float(y[1].strip()), float(y[2].strip()))
			x = studentfiles.readline()
		studentfiles.close()

	


         