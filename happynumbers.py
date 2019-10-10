f=open("1.txt","w")
for num in range(2,1000):
    if all(num%i!=0 for i in range(2,num)):
       f.write(str(num)+' ')
f.close()

f1=open("2.txt","w")
def isHappyNumber(num):    
    rem = sum = 0;    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
            
   
for i in range(1, 1001):    
    result = i;    
    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    
        
    if(result == 1):    
        f1.write(str(i)+' ')    

f1.close()
print("\nPRIME NUMBERS BETWEEN 1-1000 \n")
f=open("1.txt","r")
primes=f.read()
li_prime=primes.split(' ')
print(li_prime)

print("\nHAPPY NUMBERS BETWEEN 1-1000 \n")
f1=open("2.txt","r")
happy=f1.read()
li_happy=happy.split(' ')
print(li_happy)

print("\n\nCOMMON NUMBERS:")
for i in li_prime:
    if i in li_happy:
        print(i,end=",")
