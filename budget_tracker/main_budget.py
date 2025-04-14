# TODO: Import Budget and Transaction classes
from budget import Budget
from transaction import Transaction

def main():
    budget = Budget()
    budget.load_from_file("budget_data.txt")

    while True:
        print("\n1. Add Transaction\n2. View Summary\n3. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # TODO: Get input and create Transaction
            # TODO: Add transaction to budget
            transaction = Transaction(input('Enter a description: '),
                                      float(input('Enter an amount: ')),
                                      input('Enter a category: '),
                                      input('Is this income, True/False: '))
            
            budget.add_transaction(transaction)
            

        elif choice == "2":
            # TODO: Print each transaction
            # TODO: Print current balance
            
            for list in budget.transactions:
                if list.is_income.lower() == 'true':
                    print(list)
                else:
                    expense = str(list).replace("Income:", "Expense:")
                    #expense = f"Expense: {transaction.description} | £{transaction.amount} | Category: {transaction.category}"
                    print(expense)
            
            balance = budget.get_balance()
            print(f"£{balance}")
            

        elif choice == "3":
            budget.save_to_file("budget_data.txt")
            print("Saved! Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
