l=[]
size=int(input("Enter the number: "))
for i in range(size):
    n=int(input("Enter the number: "))
    l.append(n)
print(l)
c=0
k=int(input("Enter the key: "))
for i in l:
    c+=1
    if(i==k):
        print("Key found at position:",c)
        break
else:
    print("Key not found")'''
