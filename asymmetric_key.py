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
    #p = random.randrange(2**(n-1)+1, 2**n-1)
    while(True):
        flag = False
        p = random.randrange(2**(n-1)+1, 2**n-1)
        for i in range(len(prime_list)):
            if p%prime_list[i]==0:
                flag = True
                break
        if(not flag):
            return p

def encrypt(p):
    return p**e%n

def decrypt(c,d):
    return c**d%n

prime_list = [i+1 for i in range(1,1000)]
PrimeList()
p = generatePrime(10)
q = generatePrime(10)
n = p * q
phi_n = (p-1) * (q-1)
print("P:" , p)
print("Q:" , q)
print("n:" , n)
print("phi:", phi_n)
e = random.randrange(2,phi_n)
d = None

i = 0

while(i==0 or e%(p-1)==0 or e%(q-1)==0):
    e = random.randrange(2,phi_n)
    while(d==None):
        try:
            e = random.randrange(2,phi_n)
            d = pow(e, -1, phi_n)
        except ValueError:
            d = None
    i+=1

print("e:", e)
print("d:", d)


rand_num = random.randrange(0,1000)
C = encrypt(rand_num)
P = decrypt(C, d)

print("Ciphertext:", C)
print("Plaintext:", P)

if P==rand_num:
    print("VERIFIED")
else:
    print("INCORRECT")