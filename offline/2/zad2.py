from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None
    



def qsort( L ):
  first=p=L
  if p.next!=None:
    while p.next!=None:
      p=p.next

    q=p.value
    piwot=piwot1=p # piwot1 to stały wskaznik na piwot
    p=first
    pp=ppiwot=None  # poprzednicy p oraz piwota

    while p!=piwot1:
      if p.value>q:
        if pp==None:
          piwot.next=p
          p=p.next
          first=p
          piwot=piwot.next
          piwot.next=None
        else:
          piwot.next=p
          p=p.next
          piwot=piwot.next
          piwot.next=None
          pp.next=p
      else:
        pp=p
        ppiwot=p
        p=p.next

    if ppiwot!=None:
      ppiwot.next=None
      x=qsort(first)
      first=x
      while x.next!=None:
        x=x.next
      y=qsort(piwot1)
      x.next=y
    else:
      qsort(piwot1)

  return first





def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  
  
  

seed(42)

n = 10
# T = [ randint(1,10) for i in range(10) ]
T= [23, 0, 14, 0, 75, 60, 53, 101, 133, 78, 131, 78, 219, 202, 228, 156]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

