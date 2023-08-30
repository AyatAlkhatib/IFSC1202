#approx 365 days in a year 
#approx 52 weeks in a year

Value =int(input("Enter Length of Time in days:"))         #we want the results in integiers. 
years= int(Value//365)                 #calculate years is value of the length time in days and floor divided by the number of days in a year                   
print("years:", years)              
weeks= int(Value-years)//7           #calculate weeks is value minus the result of years and then floor divided by the number of days in weeks 
print("weeks:", weeks)
days= int(Value%years//weeks)
print("days:",days)
      













