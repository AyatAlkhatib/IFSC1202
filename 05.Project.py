a= int(input("Enter Start Of Range: "))                                 # a representing the start value
b= int(input("Enter End Of Range: "))                                    #b representing the end value
print ("Special Numbers between", a, "and", b)                          # the "and" represents the spac between the start value and end value
for i in range (a, b + 1): 
    n=i
    length = 0                             # we want the length to calculate power of the digits 
    while n > 0:
        n= n // 10
        length = length +1 
    n=i
    results = 0  
    while n > 0: 
        digits= n % 10 
        results = results + digits** length       # we want to find the whole results of the digitsl to the power of given length
        n= n // 10 
    
    if results == i: 
        print(i)



