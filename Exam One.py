a= (input("Enter Start of Range: "))
b= (input("Enter End of Range: "))
c= ("Super Special Numbers between:, a, "and", b")
for i in range (a, b + 1): 
    n=i 
    length= 0 
    while n>0:
        n= n//10
        length= length +1 
    
    n=i 
    results = 0  
    while n>0: 
        digits= n % 10 
        results = results + digits** length 
        n= n// 10 
    
    if results == i: 
        print (i)




