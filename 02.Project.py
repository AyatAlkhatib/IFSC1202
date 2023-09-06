#Equailateral= all sides are equal 
#Isoclec= two sides are equal 
#Scalene= none of the sides are equal 
#Calaculate the area using hebrons formula
#A reprsents side 1
#B reprsents side 2
#C reprsents side 3 
#P reprsents Perimeter 
#S reprsents Semiperimeter 

A=float(input("Enter side 1: "))     #our sides need to be in float form             
B=float(input("Enter side 2: "))
C=float(input("Enter side 3: "))
P= float(A + B + C)                           #Calculate Perimeter is Adding all three sides 
S= float(P/2)                                 #Calculate Semiperimeter by diving the results of the perimeter by 2 since we want half of P
area= float(S*(S-A)*(S-B)*(S-C))**0.5         #Calculate the squre root by multiplying the reults of S by the out comes of the results of S minus the sides thento the squre root of 0.5 #in this context 0.5 is equvalient to squre rooting. 
print ("area:", area)                    #the area must be float form 
