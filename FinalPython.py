def SendMoney(balance=30):
    
    Amount = float(input("Enter the amount you want to send: $"))
    
    if Amount > balance:
        print("You do not have enough money in your account.")
   
    else:
        print("Your payment was successful.")

SendMoney()


    