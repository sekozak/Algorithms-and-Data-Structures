from copy import deepcopy
from queue import PriorityQueue
from math import inf

#odczytywanie wyniku z tablicy parentow
def prnt(p, q):
  if p[q]==-1: return [q]
  return prnt(p, p[q])+[q]

#funkcja ta dziala podobnie do algorytmu dijkstry tylko zamiast trasy pokonanej do tej pory zapisuje
#maxymalna przepustowosc napotkana do tej pory
def max_extending_path( G, s, t ):
  n=len(G)
  value=[0]*n
  parent=[-1]*n
  value[s]=inf
  q=PriorityQueue()
  q.put((0, s))

  while not q.empty():
     v, p=q.get()
     for i in G[p]:
        j=i[0]
        c=value[j]
        value[j]=max(value[j], min(value[p], i[1]))
        if value[j]!=c: #wierzcholek dodaje do kolejki tylko wtedy kiedy wynik w nim jest lepszy niz obecny
          parent[j]=p
          q.put((-value[j], j))

  tab=prnt(parent, t)#funckja odtwarza trase najwiekszej przepustowosci do t, jesli poczatkiem tej trasy nie bedzie s to znaczy ze nie ma trasy z s do t
  if tab[0]!=s: return []
  return tab
  
  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")