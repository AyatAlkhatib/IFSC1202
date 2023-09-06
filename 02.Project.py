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
area= float(S*(S-A)*(S-B)*(S-C))**0.5  #Calculate area by multiplying the the result S by the out comes of S minus the three sides then mulitplaying it by 0.5 #in this context 0.5 is equalivelnt to taking a squre root
print ("area:",area)                    #the area must be float form 
