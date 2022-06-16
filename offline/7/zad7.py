from queue import PriorityQueue

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]


def quicksort(T, t, l, r):
  while l < r:
    q = partition(T, t, l, r)
    if q - l <= r - q:
      quicksort(T, t, l, q - 1)
      l = q + 1
    else:
      quicksort(T, t, q + 1, r)
      r = q - 1
  return T

def partition(T, t, l, r):
  x = T[r]
  i = l - 1
  for j in range(l, r):
    if T[j] < x:
      i += 1
      T[i], T[j] = T[j], T[i]
      t[i], t[j] = t[j], t[i]
  T[r], T[i + 1] = T[i + 1], T[r]
  t[r], t[i + 1] = t[i + 1], t[r]
  return i + 1

def read(T, x): #ta funkcja odtwarza kod huffmana od tyłu z tablicy T
  t = []
  while T[1][x] != -1:
    t.append(T[0][x])
    x = T[1][x]

  print(*t[::-1], sep='')
  return len(t)


#Tworze tablice dwuwymiarową T z wartosciami F, nastepnie szukam dwie najmiejsze liczby w T[0] i dopisuje ich sume na koniec,
#a w polach T[1] wpisuje wskazania na indeks sumy danych liczb. Mniejsza z tych liczb zmienia sie w 0, a wieksza w 1.
#Pętla wykonuje sie dopoki wszyskie liczby z T[0] nie maja wskaznania na jakis index w T[1].
def huffman( S, F ):
  wynik=0
  kopia=S[:]
  quicksort(F,S,0,len(S)-1)
  n = len(S)
  T = [[-1] * ((n*2)-1) for _ in range(2)]
  for i in range(n):
      T[0][i] = F[i]

  maks=sum(F)
  end=n
  start=0
  while end<(2*n)-1:
      a=maks; b=maks
      aix=0; bix=0
      for i in range(start,end):
          if T[0][i]<a and T[1][i]==-1:
              b=a
              bix=aix
              a=T[0][i]
              aix=i
          elif T[0][i]<=b and T[1][i]==-1:
              b=T[0][i]
              bix=i

      T[0][end]=a+b
      T[1][aix] = end
      T[1][bix] = end
      T[0][aix] = 0
      T[0][bix] = 1
      end+=1
      start+=1


  for q in kopia: #wypisuje wyniki w kolejnosci z talbicy S
      x=S.index(q)
      z=read(T,x)
      wynik+=z*F[x]

  print(wynik)
  pass
  

huffman( S, F )