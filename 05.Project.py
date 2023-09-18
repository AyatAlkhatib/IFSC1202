a= (input("Enter Start Of Range: "))
b= (input("Enter End Of Range: "))
c= (input("Special Numbers between 1 and 10000"))
number_of_digits = 0
for N in range (a,b)
while N >0: 
    N//=10 
    number_of_digits + 1 
    results = 0 
if N>0: 
    digits= N % 10
    results = digits**number_of_digits
    print(results)
    



