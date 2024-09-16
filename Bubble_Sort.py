a=[5,8,6,9,15,25,63]
print("Unordered list: ",a)
for n in range(len(a)-1,0,-1):
  for i in range(n):
    if a[i]>a[i+1]:
      temp=a[i]
      a[i]=a[i+1]
      a[i+1]=temp
print("Ordered list: ",a)
