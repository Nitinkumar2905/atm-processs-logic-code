class Bank:
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open('transaction_string', 'a', encoding='utf-8') as passbook:
            passbook.write(
                f'{transaction_string}\t\t\t new balance {self.balance}\n')

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f'withdrew $ {amount}')

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f'deposited $ {amount}')


account = Bank(50.50)
while True:
    print(f'Your account balance is : ${account.balance}')
    try:
        action = input('What kind of action do you want to take? "withdrawal" or "deposit" \n')
    except KeyboardInterrupt:
        print("Logged off!")
        break
    
    if action in ["withdrawal", "deposit"]:
        if action == "withdrawal":
            amount = float(input("How much do you want to withdraw? \n"))
            if amount > account.balance:
                print("Insufficient balance")
                break
            account.withdrawal(amount)
        else:
            amount = float(input("How much do you want to deposit? \n"))
            account.deposit(amount)
        
        if amount <= account.balance:
            print(f'Your balance is: {account.balance} $')
    else:
        print('Not a valid action')
