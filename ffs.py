import random

def GCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x



def PrimeList():
    i = 0
    while(i<len(prime_list)):
        j = i+1
        while(j<len(prime_list)):
            if(prime_list[j]%prime_list[i]==0):
                prime_list.pop(j)
                j-=1
            j+=1
        i+=1

def generatePrime(n):
    p = random.randrange(2**(n-1)+1, 2**n-1)
    while(True):
        flag = False
        p = random.randrange(2**(n-1)+1, 2**n-1)
        for i in range(len(prime_list)):
            if p%prime_list[i]==0:
                flag = True
                break
        if(not flag):
            return p
        

prime_list = [i+1 for i in range(1,1000)]
PrimeList()

k=3

p = generatePrime(10)
q = generatePrime(10)
n = p * q
print("P:" , p)
print("Q:" , q)
print("n:" , n)
s=[]
v=[]


for i in range(k):
    temp = random.randrange(2,n-2)
    temp1 = None
    while(temp1 == None):
        try:
            while(GCD(temp,n)!=1):
                temp = random.randrange(2,n-2)
            t = temp**2
            temp1 = pow(t, -1, n)
        except ValueError:
            temp1 = None
    s.append(temp)
    v.append(temp1)
    

print("S:", s)
print("V:", v)

r = random.randrange(1,n-1)
x = r**2 % n
c=[]
for i in range(k):
    c.append(random.randrange(0,2))

y = r
for i in range(k):
    y*=(s[i]**c[i])

y = y % n

print("x:", x)
print("y:", y)

check = y**2
for i in range(k):
    check *= (v[i]**c[i])
check = check % n
    
print("Check Value:", check)

if check == x:
    print("Probable")
else:
    print("Improbable")