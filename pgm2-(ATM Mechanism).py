import random
print("Welcome!")
pin1=int(input("Enter your pin: "))
pin=2003
if pin1==pin:
    otp=random.randint(1000,9999)
    print(otp)
    otp1=int(input("Enter the otp: "))
    if otp1==otp:
        while True:
            print("1.Check Balance\n2.Withdraw Amount\n3.Exit")
            opt=int(input("Enter your option: "))
            balance=10000
            if opt==1:
                print(balance)
            elif opt==2:
                amount=int(input("Enter the amount to be withdrawn: "))
                if(amount<=balance):
                    print("Please wait while we process your request!")
                    print("Please collect your cash!")
                    Rem_Bal=balance-amount
                    print("Remaining Balance is: ",Rem_Bal)
                    print("Thank You! Visit again!")
                else:
                    print("Insufficient balance!")
            elif opt==3:
                print("Thank You! Visit Again!")
                exit(0)
    else:
        print("The otp you entered is wrong!!")
else:
    print("Wrong Pin!!")
