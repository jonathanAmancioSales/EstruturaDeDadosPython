#InsertionSort

#A=[5, 2, 4, 6, 1, 3]
A=[31, 41, 59, 26, 41, 58]
print(A)

for j in range(1,len(A)):
  selectedItem=A[j]
  i=j-1
  while i>=0 and A[i]>selectedItem:
    A[i+1]=A[i]
    i-=1
  A[i+1]=selectedItem

print(A)