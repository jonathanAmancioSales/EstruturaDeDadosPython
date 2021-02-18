#InsertionSort

A=[31, 41, 59, 26, 41, 58, 101, 0, 1]
print(A)

def InsertionSort(L,inverse=False):
  for j in range(1,len(A)):
    selectedItem=A[j]
    i=j-1
    Condition=A[i]>selectedItem
    if inverse==True: Condition=A[i]<selectedItem
    while i>=0 and Condition:
      A[i+1]=A[i]
      i-=1
    A[i+1]=selectedItem
  return L

print()
print( InsertionSort(A) )
print( InsertionSort(A,True) )