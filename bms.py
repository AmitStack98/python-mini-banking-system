class BankAccount:

    # create bank Bank Account

    next_account_no = account_no = 100000000000

    def __init__(self, cos_name, balance = 0 ):
        self.cos_name = cos_name
        self.account_no = BankAccount.next_account_no + 1
        self.balance = balance    
        self.transaction = []

        BankAccount.next_account_no += 1 

    def Show_deatils(self):
        print("========== Account Deatils ==========")

        print(f"Account Holder Name: {self.cos_name}")
        print(f"Account Number: {self.account_no}")
        print(f"Available Account Balance: ₹{self.balance}")

        print("=====================================")
        
    # Deposit 

    def deposit(self):
        print("========== Ammount Deposit Status ==========")

        print("Deposit process started")
              
        Deposit_amount = int(input("Enter The Deposite Ammount: "))

        if(Deposit_amount <= 0):
            print(f"Invalid Deposit Ammount: {Deposit_amount}")
        elif(Deposit_amount < 500):
            print("Minimum Deposit Amount is ₹500")
        else:
            self.balance += Deposit_amount

            # transaction deposit amount

            self.transaction.append({
                "type":"Deposit",
                "amount":Deposit_amount
            })

            print("Deposit Successful")
            print(f"Total Balance: {self.balance}")

        print("===========================================")
    
    # withdraw

    def withdraw(self):
        print("========== Ammount Widrowal Status ==========")

        print("withdrawal process started")

        withdrawal_amount = int(input("Enter The withdrawal Ammount: "))

        if(withdrawal_amount <= 0):
            print(f"Invalid Ammount: {withdrawal_amount}")
        elif(withdrawal_amount > self.balance):
            print(f"Insufficient Balance")
        else:
            self.balance -= withdrawal_amount

            # transaction deposit amount

            self.transaction.append({
                "type":"Withdrawal",
                 "amount": withdrawal_amount
            })

            print(f"Withdrawal Successful!")
            print(f"Remaining Balance: ₹{self.balance}")    

        print("=============================================")

    # Transaction History

    def transaction_history(self):
        print("========== Transaction History ==========")

        if not self.transaction:
            print("No transactions found.")

        for tr in self.transaction:
            if tr["type"] == "Deposit":
                print(f"Deposit: ₹{tr['amount']}")
            else:
                print(f"Withdrawal: ₹{tr['amount']}")

        print("=========================================")

    def check_balance(self):
        print("========== Account Balance ==========")

        print(f"Account Holder: {self.cos_name}") 
        print(f"Account Number: {self.account_no}")
        print(f"Available Balance: ₹{self.balance}")

        print("=====================================")

account1 = BankAccount("Amit")

while True:
        print("========== MINI BANKING SYSTEM ==========")

        print("1. Show Account Details")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction Histor")
        print("6. Exit")

        print("=========================================")

        user = int(input("Enter Your Choice (1-6): "))

        if(user == 1):
            account1.Show_deatils()
        elif(user == 2):
            account1.deposit()
        elif(user == 3):
            account1.withdraw()   
        elif(user == 4):
            account1.check_balance()   
        elif(user == 5):
            account1.transaction_history()
        elif(user == 6):
            print("==================================")

            print("Thank you for banking with us! 🏦")
            print("Your trust is our priority.")
            print("Have a great day! 😊")
            
            print("==================================")
            break
        else:
            print("Please Select Valid Option!..")





# Method Call

# Account Holder Name
# account1 = BankAccount("Amit")
# account2 = BankAccount("Krish")
# account3 = BankAccount("bhavesh")

# Account Holder Deatils Show
# account1.Show_deatils()
# print("_________________")

# account2.Show_deatils()
# print("_________________")

# account3.Show_deatils()
# print("_________________")

# Deposit 

# account1.deposit()
# account2.deposit()
# account3.deposit()


# withdraw

# account1.withdraw()
# account1.transaction_history()
# account1.check_balance()