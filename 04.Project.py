# a represents the start range 
# b represents the end range 
# c reprsents the prime number of the start of a and end of b 
# N reprsents the numbers in the ranges from start to end 
# i reprsents the equation we are using to figure our prime numbers 
# we will need a break when if moldues n of i is equal to zero 
# if it doesn't equal to zero then its a prime number
a= int(input("Enter Start of Range: "))             
b= int(input("Enter End of Range: "))
c= (input ("Prime Numbers between 50 and 100"))
for N in range (a,b):
    for i in range (2,int(N/2)+1):
        if N % i ==0: 
            break
    else: 
        print(N)


           


