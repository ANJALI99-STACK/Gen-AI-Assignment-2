balance = 10000
MIN_BALANCE = 500
def atm(balance):
    while True:
        print("\nATM SIMULATOR")
        print("1. check Balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("current Balance: ₹", balance)
        elif choice == 2:
            amount = int(input("enter amount to deposit: "))
            balance = balance + amount
            print("deposit successful!")
            print("new balance: ₹", balance)
        elif choice == 3:
            amount = int(input("enter amount to withdraw: "))
            if balance - amount >= MIN_BALANCE:
                balance = balance - amount
                print("withdrawal successful!")
                print("New balance: ₹", balance)
            else:
                print("insufficient balance!")
                print("minimum ₹500 must be maintained.")
        elif choice == 4:
            print("exited")
            break
        else:
            print("invalid choice!")
    return balance
balance = atm(balance)