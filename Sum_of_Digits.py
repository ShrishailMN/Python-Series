n=int(input("Enter the number: "))
digitSum=0
while n>0:
  last_digit=n%10
  n=n/10
  digitSum+=int(last_digit)
print(digitSum)
