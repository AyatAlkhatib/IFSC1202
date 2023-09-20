a= int(input("Enter Start of Range: "))
b= int(input("Enter End of Range: "))
print ("Super Special Numbers between", a, "and", b)
for i in range (a, b + 1): 
    n=i
    while n > 0:
        n= n // 10
    n=i
    results = 0  
    while n > 0: 
        digits= n % 10 

# compute factorial of digits
        prod = 1
        for  j in range (1, digits +1):                          # we are calcuating the factorial
            prod = prod * j


        results = results + prod                                 
        n= n // 10 
    
    if results == i: 
        print(i)
    






