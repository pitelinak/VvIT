
'''f=open('Задание_17__ahsu__rjf4.txt')
a=[]
k=0
maxim=0
for x in f:
    a.append(int(x))
for i in range (len(a)-1):
    if ((a[i]+a[i+1])%10==5 and (a[i]+a[i+1])%35==0):
        k+=1
        l=a[i]*a[i+1]
        if (l%10==0):
            if (l>maxim):
                maxim=l
print(k,maxim)

a=[0]*40
a[1]=1
for i in range (2,35):
    a[i]=a[i-3]+a[i//4]

print (a[34])

from functools import lru_cache

def moves(h):
    return h+1,h*2

@lru_cache (None)

def f(h):
    if (h>=165):
        return 'end'
    if (any(f(x)=='end' for x in moves(h))):
        return 'win1'
    if (all(f(x)=='win1' for x in moves(h))):
        return 'lose1'
    if (any(f(x) == 'lose1' for x in moves(h))):
        return 'win2'
    if (all(f(x) == 'win2' or f(x)=='win 1' for x in moves(h))):
        return 'lose2'

for s in range (1,170):
    print (s,f(s))

'''
'''
from functools import lru_cache

def moves(h):
    return h+1,h*2

@lru_cache (None)

def f(h):
    if (h>=31):
        return 'end'
    if (any(f(x)=='end' for x in moves(h))):
        return 'p1'
    if (all(f(x)=='p1' for x in moves (h))):
        return 'v1'
    if (any(f(x) == 'v1' for x in moves(h))):
        return 'p2'
    if (all(f(x) == 'p1' or f(x)=='p2' for x in moves(h))):
        return 'v2'

for x in range (1,300):
    print(x,f(x))

'
from functools import lru_cache

def moves(h):
    return h+2,h*2

@lru_cache (None)
def f(h):
    if h>=55:
        return 'end'
    if (any(f(x)=='end' for x in moves(h))):
        return 'p1'
    if (all(f(x)=='p1' for x in moves (h))):
        return 'v1'
    if (any(f(x)=='v1' for x in moves(h))):
        return 'p2'
    if (all(f(x)=='p1' or f(x)=='p2' for x in moves (h))):
        return 'v2'

for x in range (1,100):
    print(x,f(x))


from functools import lru_cache

def moves(h):
    a,b=h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

@lru_cache (None)
def f(h):
    if (sum(h)>=47):
        return 'end'
    if (any(f(x)=='end' for x in moves(h))):
        return 'p1'
    if (all(f(x)=='p1' for x in moves (h))):
        return 'v1'
    if (any(f(x)=='v1' for x in moves(h))):
        return 'p2'
    if (all(f(x)=='p1' or f(x)=='p2' for x in moves (h))):
        return 'v2'


for x in range (1,100):
    h=4,x
    print(x,f(h))


s=open('Задание_6_ДЗ.txt').read()

k=0
maxim=0
for i in range (len(s)-1):
    if (s[i]!=s[i+1]):
        k+=1
        if (k>maxim):
            maxim=k
    else:
        k=0

print(maxim)


for n in range(190201,190230+1):
      divs = [] # чистим список делителей
      for d in range(1,n+1): #
        if n % d == 0:
          divs = divs + [d] # добавляем делитель в список
          if len(divs) > 4: break
      if len(divs) == 4:
        divs.reverse()
        print(divs)




print ('x','y','z','w')
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                if not((x==z) or (not(z) and y) or (not(w))):
                    print (x,y,z,w)


n=42**42+4**22+4-1
k=0
while n>0:
    if n%2==0:
        k+=1
        n=n//2

print(k)


def f(x,y,a):
    return (x<=a) or (y<a) or ((x*y)%4==0) or (y*y>10**6) or (x*x>10**4)
for a in range (0,100000):
    if (all(f(x,y,a)==1 for x in range(1,100000) for y in range (1,100000))):
        print(a)


n=3*4**38+2*4**23+4**20+3*4**5+2*4**4+1
k=0
while n>0:
    if n%16==0:
        k+=1
    n=n//16
print(k)

def f(n):
    if n==50:

        return 1
    if n>50:
        return 0
    if n<50:
        return f(n+2)+f(n*5)

print (f(2))



def f(n):
    if n==16:
        return 1
    if (n>16) or (n==6) or (n==12):
        return 0
    else:
        return f(n+1)+f(n*2)+f(n+3)

print(f(3))


def f(n):
    if n==11:
        return 1
    if n>11:
        return 0
    if n<11:
        return f(n+1)+f(n+2)+f(n*2)

print (f(4))

def f(n):
    if n==13:
        return 1
    if n>13:
        return 0
    else:
        return f(n+1)+f(n+2)+f(n*2)

print(f(11))


s=[]
def f(n,k):
    if k==10:
        s.append(n)

    elif k>10:
        return
    else:
        return f(n+2,k+1) or f(n+3,k+1)

f(2,0)

print(len(set(s)))


s=[]
def f(n,k):
    if k==28:
        s.append(n)

    elif k>28:
        return
    else:
        return f(n+17,k+1) or f(n+35,k+1)

f(1,0)

print(len(set(s)))

def f(n):
     if n==5:
         return 1
     if (n<5) or n==14 or n==21:
         return 0
     if n>5:
         return (f(n-1)+f(n-2))

print (f(26))


def f(n):
    if n<3:
        return n
    if n>2:
        return f(n-1)*f(n-3)+2*f(n-3)

print (f(6))


f=open('')
a=[]
for x in f:
    a.append(int(x))
k=0
maxim=0
for i in range (len(a)-1):


f=open()
n=int(f.readline())
a=[]
for s in f:
    a.append(int(s))
a.sort(reverse=True)
uchet_corobok=[a[0]]
for i in range (1,n):
    if kladem[-1] - a[i] >=5:
         kladem.append(a[i])

print(len(kladem), min(kladem))

'''

sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides = sorted(sides, reverse=True)
smax = 0
for i in range(len(sides)):
for j in range(i + 1, len(sides)):
for k in range(j + 1, len(sides)):
a = sides[i]
b = sides[j]
c = sides[k]
if a + b > c and a + c > b and b + c > a:
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
if s > smax:
smax = s
print("Максимальная площадь треугольника", smax)




