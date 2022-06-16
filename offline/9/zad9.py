from copy import deepcopy
from math import inf

class Node:
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.parent=self

def find(x):
    if x!=x.parent:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y: return 1
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank: y.rank+=1

def cykl(A,B1):
    n=len(A)-1
    t=[A[n][0],A[n][1]]
    suma=B1[n]
    while t[0]!=t[len(t)-1]:
        for i in range(n):
            if A[i]!=0:
                l=len(t)-1
                if A[i][0]==t[l]:
                    t.append(A[i][1])
                    A[i]=0
                elif A[i][1]==t[l]:
                    t.append(A[i][0])
                    A[i]=0
                suma+=B1[i]

    return t[1:],suma

#dzieki tablicy t2 zawierajacej stopnie wierzcholkow oraz zamiennej y z iloscia nieparzystych wierzcholków
#moge usunąc krawedzie dołaczone do cyklu
def repair(B,y,t2):
    n=len(B)
    while y!=0:
        for i in range(n):
            if B[i]!=0:
                a=B[i][0]
                b=B[i][1]
                if t2[a]==1 or t2[b]==1:
                    t2[a]-=1
                    t2[b]-=1
                    if t2[a]%2==1: y+=1
                    else: y-=1
                    if t2[b]%2==1: y+=1
                    else: y-=1
                    B[i]=0

#korzystam z algorytmu Kruskala i gdy pojawi mi sie cykl to sprawdzam jego dlugosc
#nastepnie funkcja repair usuwa krawedzie z tablicy B nie bedace czescia cyklu
#na koniec funkcja cykl tworzy tablice w wierzcholkami cyklu i sume
def min_cycle( G ):
    n=len(G)
    t=[];punkty=[];A=[];A1=[]
    k=0;suma=inf
    for i in range(n):
        for j in range(i, n):
            if G[i][j]!=-1:
                t.append((G[i][j], i, j))
                k+=1
    t.sort(key=lambda t: t[0])

    for i in range(n): punkty.append(Node(i))

    wynik=[]
    for i in range(k):
        a=punkty[t[i][1]]
        b=punkty[t[i][2]]

        if union(a, b)==1:
            t2=[0]*n;y=0
            B=deepcopy(A)
            B1=deepcopy(A1)
            B.append((t[i][1], t[i][2]))
            B1.append(t[i][0])
            for j in B:
                if j!=0:
                    t2[j[0]]+=1
                    t2[j[1]]+=1
                    if t2[j[0]]%2==1: y+=1
                    else: y-=1
                    if t2[j[1]]%2==1: y+=1
                    else: y-=1

            if y!=0: repair(B, y, t2)

            odp, s=cykl(B, B1)
            if s<suma:
                wynik=odp
                suma=s

        else:
            A.append((t[i][1], t[i][2]))
            A1.append(t[i][0])

    return wynik
  
  

### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]  
LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")
  
