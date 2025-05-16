print("welcome to state bank of india")
user=input("enter your card:")
pin=2345
amt=60000
if user=="yes":
    userpin=int(input("enter your pin:"))

    if userpin==pin:
        user2=input("select the mode of transaction [ withdraw, checkbalance ]")
        if user2=="withdraw":
            amt=int(input("enter your amount:"))

            if amt<=50000:
                print("transaction successful")
            else:
                print("failed")

        if user2=="checkbalance":
            print("balance:", 80000)
    else:
        print("wrong pin")
