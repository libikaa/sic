import random

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
print("P:" , p)
print("Q:" , q)
print("n:" , n)
s = random.randrange(2,n-2)
v = s**2 % n

print("s:" , s)
print("v:" , v)

r = random.randrange(1,n-1)
x = r**2 % n
c = random.randrange(0,2)
y = r * (s**c) % n

print("x:" , x)
print("y:" , y)

check_1 = y**2 % n
check_2 = x*(v**c) % n

print("VALUES TO BE COMPARED:", check_1, ",", check_2)

if check_1 == check_2:
    print("Probable")
else:
    print("Improbable")