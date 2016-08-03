import math

def isprime(num):
    if(num==2):
        return 1
    elif(num%2==0):
        return 0
    else:
        
        i=3       
        while(i<=int(math.sqrt(num))):
            
            if(num%i==0):
                return 0
            i=i+1
    
    return 1
#if(isprime(51)==1):
#    print(isprime(51))

count=0
j=2
while(count<1000):
    
    if(isprime(j)==1):
        #
        count=count+1;
        print("%d is prime!" % (j))
    
    j=j+1;
 
print("The 1000th prime is %d" % (j-1) )     