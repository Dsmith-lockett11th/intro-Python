def SendMoney(balance=30):
    
    AmountSent = float(input("Enter the amount you want to send: $"))
    
    if AmountSent > balance:
        print("You do not have enough money in your account.")
   
    else:
        print("Your payment was successful.")

SendMoney()


    