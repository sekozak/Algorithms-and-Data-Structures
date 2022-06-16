from copy import deepcopy

def DFS(G, p, kra):
    #ta funkcja szuka trasy dopoki ma krawedzie z punktu p oraz usuwa krawedzie po ktorych juz przeszła,
    #a na koncu zwraca rekurencyjnie tablice z odwiedzonymi punktami
    n=len(G[0])
    for j in range(n):
        if G[p][j]==1 and kra[p][j]==1:
            kra[p][j] = 0
            kra[j][p] = 0
            return [j]+DFS(G,j,kra)
    return []

def glue(t):
    #to funckja do sklejania tras znalezionych przez funkcje DFS w cykl eulera, jesli taki istnieje
    lista=t.pop(0)
    for _ in range(len(t)):
        lista1=t.pop(0)
        if lista1[0] not in lista: return None #jesli kolejny cykl nie bedzie mial ani jedngo pujnktu wspolnego to graf bedzie niespojny
        ix=lista.index(lista1[0])
        tab=[]
        for i in range(len(lista)):
            if i==ix:
                for j in lista1:
                    tab.append(j)
            else: tab.append(lista[i])
        lista=tab[:]

    return lista

def euler( G ):
    n=len(G[0])
    kra=[]*n
    for y in G: #tworze kopie G aby moc usuwac uzyte krawedzie
        kra.append(y[:])
        x=sum(y)
        if x==0 or x%2==1: #sprawdzam wstepnie czy graf bedzie mogl miec cykl eulera
            return None

    wynik=[]
    suma=0
    bool=True
    while bool:
        bool=False
        suma=0

        i=-1
        for e in range(n):
            suma+=sum(kra[e])
            if i==-1 and sum(kra[e])>0: #szukam koljenego punktu z ktorego dalej wychodzi krawedz
                i=e

        if suma>=6: bool=True #z mniej niz 3(w macierzy G jest 2 razy wiecej jedynek niz krawedzi) krawedzi nie mozna stworzyc kolejnego cyklu

        if bool:
            tab=[i]+DFS(G, i, kra)
            wynik.append(tab)

    if suma==0: #nie moze zostac wolna krawdz bez cyklu, aby stworzyc cykl eulera
        return glue(wynik)
    return None
  
  


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]


GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")