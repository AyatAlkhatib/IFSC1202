a= int(input("Enter Start of Range: "))
b= int(input("Enter End of Range: "))
c= (input ("Prime Numbers between 50 and 100"))
for N in range (a,b):
    for i in range (2,int(N/2)+1):
        if N % i ==0: 
            break
    else: 
        print(N)


           


