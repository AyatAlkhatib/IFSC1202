#approx 365 days in a year 
#approx 52 weeks in a year
#7 reprsents the number of days in a week 
#we want the results in integiers. 
Value =int(input("Enter Length of Time in days:"))         
Years= int(Value//365)                 #calculate years is value of the length time in days and floor divided by the number of days in a year                   
print("Years:", Years)              
Weeks= int(Value % 365) //7            #Calculate weeks is value of the length time in days and take moloduls of 365 then floor divided by 7 days in a week
print("Weeks:", Weeks)
Days= int(Value%365)%7             #calculate days is value of the length in days and take moloduls of 365 then take the moloduls of 7 days in a week
print("Days:",Days)
      














