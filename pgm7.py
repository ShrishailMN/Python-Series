n=int(input("Enter the number: "))
for i in range(2,n-1):
  if n%i==0:
    print("Not a prime number")
    break
else:
   print("Prime Number")
