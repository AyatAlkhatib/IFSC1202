a= (input("Enter Start Of Range: "))
b= (input("Enter End Of Range: "))
c= (input("Special Numbers between 1 and 10000"))
digits_num = 0
for I in range (a,b+1):
    N=I
    while N>0: 
    digits_num = digits_num + 1 
    results = 0 
if N>0: 
    digits= N % 10
    results = digits**number_of_digits
    print(results)
    



