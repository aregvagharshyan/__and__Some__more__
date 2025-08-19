# Implement an AdvancedBankSystem class with the following methods:
# Data Structure:
# python
# Copy
# Edit
# {
#     account_number: {
#         "holder": name,
#         "balance": balance,
#         "transactions": [(type, amount)],  # Example: [("Deposit", 100), ("Withdraw", 50)]
#         "loan": (amount, interest_rate),
#     }
# }
# Methods to Implement.
# 1 create_account(account_number, holder, balance)
# Adds a new bank account.
# 2 deposit(account_number, amount)
# Adds money and records transaction.
# 3 withdraw(account_number, amount)
# Withdraws if balance allows, else denies.
# 4 get_balance(account_number)
# Returns balance.
# 5 get_transaction_history(account_number, n=None)
# Uses enumerate() to return the last n transactions (default: all).
# 6 apply_interest()
# Uses map() to apply 5% interest to all accounts with loans.
# 7 rich_accounts(threshold)
# Uses filter() to return accounts with balance above threshold.
# 8 merge_accounts(acc1, acc2, new_acc_num)
# Uses zip() to merge two accounts into one, combining transactions and balance.
# 9 account_summary()
# Uses dictionary comprehension to return {account_number: balance}.
# 10 loan_details()
# Uses list comprehension to return [("Alice", 5000, 5.5%)] for all users with loans.

class AdvancedBankSystem:

    def __init__(self):
        self.store = {}

    def create_account(self, account_number, holder, balance = 0):
        if account_number in self.store:
            raise ValueError("Account already exists!")
        self.store[account_number] = {
        "holder": holder,
        "balance": balance,
        "transactions": [],
        "loan": None
    }
        return f'{holder} with {account_number} id added to bank account'

    def deposit(self, account_number, amount):
        if account_number not in self.store:
            raise ValueError("Account not found!")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.store[account_number]['balance'] += amount
        self.store[account_number]['transactions'].append(('Deposit', amount))
        return f'{amount}-deposit is successful for {account_number} id, transaction history: {self.store[account_number]['transactions']}'

    def withdraw(self, account_number, amount):
        if account_number not in self.store:
            raise ValueError("Account not found!")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive!")
        if amount <= self.store[account_number]['balance']:
            self.store[account_number]['balance'] -= amount
            self.store[account_number]['transactions'].append(('Withdraw', amount))
            return f'{amount}-withdraw is successful for {account_number} id, transaction history: {self.store[account_number]['transactions']}'
        else:
            raise ValueError('Not enough balance for withdraw!')

    def get_balance(self, account_number):
        if account_number not in self.store:
            raise ValueError("Account not found!")
        return f'Balance for {account_number} id: {self.store[account_number]['balance']}'

    def get_transaction_history(self, account_number, n = 1):
        if account_number not in self.store:
            raise ValueError("Account not found!")
        transactions = list(enumerate(self.store[account_number]['transactions'], start = n))
        return f'Transaction for {account_number} id: {transactions}'

    def add_loan(self, account_number, loan_amount, interest_rate):
        if account_number not in self.store:
            raise ValueError("Account not found!")
        self.store[account_number]["loan"] = (loan_amount, interest_rate)
        self.store[account_number]["transactions"].append(("Loan", loan_amount))
        return f'Loan of {loan_amount} with {interest_rate}% interest added to account {account_number} id.'

    def apply_interest(self):
        def apply_loan_interest(account_data):
            loan = account_data["loan"]
            if loan:
                loan_amount, interest_rate = loan
                if loan_amount > 0:
                    new_loan_amount = loan_amount * (1 + 5 / 100)
                    new_interest_rate = interest_rate + 5
                    account_data["loan"] = (new_loan_amount, new_interest_rate)
                    account_data["transactions"].append(("Interest Applied", new_loan_amount))
                    return f"Applied interest: New loan amount: {new_loan_amount}, New interest rate: {new_interest_rate}%"
            return None
        results = map(apply_loan_interest, self.store.values())
        for result in results:
            if result:
                return result
        return f'Not results!'

    def rich_accounts(self, threshold):
        with_threshold = list(filter(lambda x: x > threshold, [i['balance'] for i in self.store.values()]))
        accounts_with_it = [i for i, j in self.store.items() if j['balance'] in with_threshold]
        return f'Accounts id with balance above threshold: {accounts_with_it}'

    def merge_accounts(self, acc1, acc2, new_acc_num):
        if acc1 not in self.store and acc2 not in self.store:
            raise ValueError('Account1 or Account2 not found!')
        new_balance = self.store[acc1]['balance'] + self.store[acc2]['balance']
        merged_transactions = list(zip(self.store[acc1]['transactions'], self.store[acc2]['transactions']))
        self.store[new_acc_num] = {
            "balance": new_balance,
            "transactions": merged_transactions,
        }
        return f'{new_acc_num} id: New account with (balance, transactions) added'

    def account_summary(self):
        summary = {acc_num: data["balance"] for acc_num, data in self.store.items()}
        return f'Account id and balance: {summary}'

    def loan_details(self):
        loan_users = [(j['holder'], j['loan'][0], f"{j['loan'][1]}%") for i, j in self.store.items() if 'loan' in j and j['loan'] is not None]
        return f'Accounts with loan: {loan_users}'

bank_system = AdvancedBankSystem()
print(bank_system.create_account(101, "Alice", 500))
print(bank_system.create_account(102, "Bob", 1000))
print(bank_system.deposit(101, 200))
print(bank_system.deposit(102, 500))
print(bank_system.withdraw(101, 150))
print(bank_system.withdraw(102, 200))
print(bank_system.get_balance(101))
print(bank_system.get_balance(102))
print(bank_system.get_transaction_history(101))
print(bank_system.get_transaction_history(102))
print(bank_system.add_loan(101, 1000, 10))
print(bank_system.apply_interest())
print(bank_system.rich_accounts(1000))
print(bank_system.merge_accounts(101, 102, 103))
print(bank_system.account_summary())
print(bank_system.loan_details())

