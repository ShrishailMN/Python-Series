print("Welcome!")
print("Please wait while we process your request")
pin=(input("Enter your pin: "))
balance=10000
if (len(pin)==4 and pin.isnumeric()):
    amount=int(input("Enter the amount to be withdrawn: "))
    if(amount<=balance):
        print("Please wait while we process your request!")
        print("Please collect your cash!")
        Rem_Bal=balance-amount
        print("Remaining Balance is: ",Rem_Bal)
        print("Thank You! Visit again!")
    else:
        print("Insufficient balance!")
else:
    print("Invalid Pin! Please Enter the valid pin")
