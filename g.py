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

p = generatePrime(10)
q = generatePrime(10)
n = p * q
phi = (p-1) * (q-1)

print("P", p)
print("Q", q)
print("n", n)
print("phi", phi)

e = random.randrange(2,n-2)
while(GCD(e,phi)!=1):
    e = random.randrange(2,n-2)
s = random.randrange(2,n-2)
v = None
while(v == None):
    try:
        s = random.randrange(2,n-2)
        t = s**e
        v = pow(t, -1, n)
    except ValueError:
        v = None
 
print("V", v)        
r = random.randrange(2,n-2) 
x = r**e % n
print("x", x)
c = random.randrange(1,e)
y = (r*(s**c)) % n
print("y", y)

check = (y**e) * (v**c) % n

print("Check value:", check)
if check == x:
    print("Probable")
else:
    print("Improbable")
