#InsertionSort

A=[31, 41, 59, 26, 41, 58, 101, 0, 1, 3.14]
print(A)

def InsertionSort(L,inverse=False):
  for j in range(1,len(A)):
    aux=A[j]
    i=j-1
    while i>=0 and (A[i]>aux)!=inverse:
      A[i+1]=A[i]
      i-=1
    A[i+1]=aux
  return L

print()
print( InsertionSort(A) )
print( InsertionSort(A,True) )