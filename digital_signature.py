import random

def RSA_sig(M):
    S = M**d % n
    return S

def RSA_ver(S):
    M_1 = S**e % n
    return M_1

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
phi_n = (p-1) * (q-1)

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

rand_num = random.randrange(0,500)
print("MESSAGE:", rand_num)
S = RSA_sig(rand_num)
print("AFTER SIGNING:", S)
M = RSA_ver(S)
print("VERFIED MESSAGE:", M)
if rand_num == M:
    print("VERIFIED")
else:
    print("INVALID")    
