class BankAccount:
    bank_name = "National Bank"

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount} deposit ho gaye. Naya balance: Rs. {self.balance}")
        else:
            print("Pese deposit karne ke liye amount 0 se bari honi chahiye.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Aap ke account me itne pese nahi hain!")
        elif amount <= 0:
            print("Sahi amount dakhil karein.")
        else:
            self.balance -= amount
            print(f"Rs. {amount} nikal liye gaye. Baqi balance: Rs. {self.balance}")

    def display_info(self):
        print(f"\n--- Account Details ({BankAccount.bank_name}) ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: Rs. {self.balance}\n")

user1 = BankAccount("Ali", 1000)
user1.display_info()
user1.deposit(500)
user1.withdraw(300)
user1.withdraw(2000)