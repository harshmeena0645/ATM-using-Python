class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number)
            return True
        return False

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        return None

    def perform_action(self, account_number, action, amount=0):
        account = self.get_account(account_number)
        if not account:
            return "Account not found."

        if action == 'check_balance':
            return f"Your balance is: ${account.check_balance()}"
        elif action == 'deposit':
            if account.deposit(amount):
                return f"${amount} deposited successfully."
            return "Invalid deposit amount."
        elif action == 'withdraw':
            if account.withdraw(amount):
                return f"${amount} withdrawn successfully."
            return "Insufficient funds or invalid amount."
        else:
            return "Invalid action."
        

def main():
    atm = ATM()

    while True:
        print("\nWelcome to the ATM")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter new account number: ")
            if atm.create_account(account_number):
                print("Account created successfully.")
            else:
                print("Account already exists.")
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            print(atm.perform_action(account_number, 'check_balance'))

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            print(atm.perform_action(account_number, 'deposit', amount))

        elif choice == '4':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            print(atm.perform_action(account_number, 'withdraw', amount))

        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
