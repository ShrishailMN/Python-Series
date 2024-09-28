a=[4,2,6,3,8,1,9,22,11]
even=[]
odd=[]
for i in a:
    if i%2!=0:
        odd.append(i)
    elif i%2==0:
        even.append(i)
print("Even Numbers: ",even)
print("Odd numbers: ",odd)
