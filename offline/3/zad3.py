from random import randint, shuffle, seed


def select(A, l, r, k):
  if l==r: return A[l]
  q=partition(A, l, r)
  if q==k:
    return A[q]
  elif k<q:
    return select(A, l, q-1, k)
  else:
    return select(A, q+1, r, k)

def isort(A, l, r): 
  for i in range(l+1, r+1):
    while A[i-1]>A[i] and i>l:
      A[i], A[i-1]=A[i-1], A[i]
      i=i-1

def partition(T, l, r):
  a=mpiatki(T, l, r)
  x=T[a]
  T[r], T[a]=T[a], T[r]
  i=l-1
  for j in range(l, r):
    if T[j]<=x:
      i+=1
      T[i], T[j]=T[j], T[i]
  T[r], T[i+1]=T[i+1], T[r]
  return i+1

def mpiatki(A, l, r):	#wyznacza index mediany potrzeby do funkcji partition jako pivot
  if (r-l)>4:  #rekurecja potrwa do poki bedzie wiecej niz 5 elementow
    p=(r-l+1)//5
    j=l
    for i in range(p):
      x=l+i*5
      isort(A,x,x+4)
      A[j], A[x+2]=A[x+2], A[j] 	#1przesuwam mediany na poczatek aby nie towrzyc niepotrzebnej tablicy
      j+=1
    if (r+1-l)%5!=0:
      isort(A, p*5+l, r)
      A[j], A[(5*p+r+l)//2]=A[(l+p*5+r)//2], A[j]  #1
      j+=1

    return mpiatki(A, l, j-1)  #wywołuje funkcje dla przesunietych median
  else:
    isort(A, l, r)
    return (l+r)//2  #index mediany

def linearselect( A, k ):
  return select(A,0,len(A)-1,k)


seed(42)
n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
    
print("OK")

