import random

def sig(M):
    S = M**d % n
    return S

def ver(S,M):
    D=hashfunction(M)
    D = int(D,2)
    M_1 = S**e % n
    if(M_1==D):
        return "VERIFIED"
    else:
        return "INCORRECT"

def decimalToBinary(n):
  return "{:08b}".format(int(n))

def db(n):
    return "{:016b}".format(int(n))
    
def xor(a,b):
    n=16
    ans = ""
    for i in range(n):
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

def hashfunction(h):
        IV=xor(h[0],h[1])
        for i in range(2,len(h)):
            IV=xor(IV,h[i])
        return IV

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
        
def message_dig(m):
    pass

prime_list = [i+1 for i in range(1,1000)]
PrimeList()
#print(prime_list)
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
    
res=[]
B=[]
i=0
Result=""
file=open("myfile.txt","rb")

byte=file.read(1)

while byte:
    
    B.append(decimalToBinary(ord(byte.decode("utf-8"))))
    if len(B)==2:
        for i in range(0,2):
            Result=Result+B[i]
        res.append((Result))
        B=[]
        Result=""
    byte=file.read(1)
print("message from file :",res)   
D=hashfunction(res)
print("after hash message ",D)
D = int(D,2)
S=sig(D)
print("Signature : ",S)    
print(ver(S,res))
