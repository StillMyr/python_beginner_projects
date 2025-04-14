# TODO: Import Transaction class from transaction.py
from transaction import Transaction

class Budget:
    def __init__(self):
        # TODO: Create a list to store transactions
        self.transactions = []

        
    def add_transaction(self, transaction):
        # TODO: Append the transaction to the list
        self.transactions.append(transaction)
    

    def get_balance(self):
        # TODO: Loop through transactions and calculate the balance
        balance = 0
        
        for transaction in self.transactions:
            if transaction.is_income.lower() == 'true':
                # print(transaction.amount)
                # print(balance)
                balance += transaction.amount
                               
            if transaction.is_income.lower() == "false":
                balance -= transaction.amount
                        
        return balance
        

    def save_to_file(self, filename):
        # TODO: Write transactions to a file
        
        with open(filename, 'w') as txt_file:
            for transactions in self.transactions:
               
                if transactions.is_income.lower() == 'true':
                    txt_file.write(f"Income: {transactions.description} | £{transactions.amount} | Category: {transactions.category}\n") 
                 
                if transactions.is_income.lower() == 'false':
                    txt_file.write(f"Expense: {transactions.description} | £{transactions.amount} | Category: {transactions.category}\n")
        

    def load_from_file(self, filename):
        # TODO: Read file and load transactions using Transaction class
        try:
            with open(filename, 'r') as txt_file:
                for current_transaction in txt_file:
                    current_transaction = current_transaction.strip()
                    description, amount, category = current_transaction.split('|')

                    if description and amount and category:
                        if description.startswith("Income: "):
                            is_income = "true"
                            new_description = description.replace("Income: ", "").strip()
                        elif description.startswith("Expense: "):
                            is_income = "false"
                            new_description = description.replace("Expense: ", "").strip()
                        
                        amount_part = float(amount.replace("£", "").strip())
                        category_part = category.replace("Category: ", "").strip()
                        
                        transaction = Transaction(new_description, amount_part, category_part, is_income)
                        self.transactions.append(transaction)

        except FileNotFoundError:
            print(f'{filename} not found')

        except Exception as e:
            print(f'An error has occured while loading: {e}')
