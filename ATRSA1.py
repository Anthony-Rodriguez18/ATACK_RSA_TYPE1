import random  

'''
def COMPUESTO(d, n):
    a = 2 + random.randint(1, n - 4)
    x = EXPMOD(a, d, n)
  
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n 
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True
    # Return compuesto
    return False

def Miller( n, s):
    if (n <= 1 or n == 4):
      return False
    if (n <= 3):
      return True
    u = n - 1
    while (u % 2 == 0):
      u//= 2
    for i in range(s):
      if (COMPUESTO(u, n) == False):
        return False

    return True
  

def PRIMO(n,s):
  for _ in iter(int, 1):
    b = random.getrandbits(n)
    if (Miller(b, s)):
      return(b)

def RSA(k):
  bit=k/2
  com = True
  while (com):
    p = PRIMO(int(bit),43)
    q = PRIMO(int(bit),43)
    if(p!=q):
      com=False
  n = (p*q)
  fin = ((p-1)*(q-1))

  d=inverso(e,fin)
  return (n,e,d)
  
def decifrado(C,N,D):
  m=EXPMOD(C, D, N)
  return m

(n,e,d)=RSA(64)
'''

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
  
def EXPMOD(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y>>1
        x = (x * x) % p

    return res

def EUCLIDES(a,b):
    if b == 0:
        return a
    else:
        return EUCLIDES(b, a%b)

def EUCLIDESEXT(a,b):
    if b == 0:
        return(a,1,0)
    else:
        (d,x1,y1) = EUCLIDESEXT(b, a%b)
        aux = a/b
        p= int(aux)
        (x,y) = (y1, x1-(p*y1))
        return(d,x,y)

def PHI(n):
  r = 0
  for i in (1,n):
    d = EUCLIDES(i, n)
    if d == 1:
      r = r + 1
  return r

def inverso(a,n):   
  if EUCLIDES(a,n) == 1:
    (p,x,y)=EUCLIDESEXT(a,n)
    m =x%n
    return m

def decifrado(C,N,D):
  m=EXPMOD(C, D, N)
  return m

def cifrado(M,N,E):
  a=EXPMOD(M, E, N)
  return a

e = 65537 
n = 999630013489
c = 747120213790

seg = True
while (seg):
  x=random.randint(0,n)
  if(EUCLIDES(x,n)==1):
    seg=False
    
fac=prime_factors(n)
p=fac[0]-1
q=fac[1]-1
fin=p*q
d = inverso(e,fin)
c1 = ((c%n)*EXPMOD(x,e,n))%n
m1 = decifrado(c1,n,d)

x1 = inverso(x,n)

m = m1*x1

mc = cifrado(m,n,e)

print("C =",c)
print("MENSAJE =",m)
print("CIFRADO =",mc)
