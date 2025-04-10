def show_balance(balance):
    print(f'Your balance is {balance:.2f}')

def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount <= 0:
        print("The amount is not valid")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print('Insufficient funds')
        return 0
    elif amount <= 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("""
                BANKING ACCOUNT
            1. Show balance
            2. Deposit
            3. Withdraw
            4. Quit

                """)
        
        user = int(input("Enter your choice: [1-4]: "))

        match user:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                is_running = False
            case _default:
                print('That is not a valid choice.')
                print("------------------------------")
    print("Have a nice day!")

if __name__ == '__main__':
     main()