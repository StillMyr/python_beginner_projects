class Transaction:
    # TODO: Create the __init__ method with:
    # description (string), amount (float), category (string), is_income (bool)
    def __init__(self, description: str, amount: float, category: str, is_income: bool):
        self.description = description
        self.amount = amount
        self.category = category
        self.is_income = is_income
        

    # TODO: Create the __str__ method to return a formatted string like:
    # "Income: Freelance Work | $250.00 | Category: Work"
    def __str__(self):
        return f'Income: {self.description} | £{self.amount} | Category: {self.category}'
    

