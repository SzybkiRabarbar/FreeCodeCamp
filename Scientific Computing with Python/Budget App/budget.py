from itertools import zip_longest

class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger = list()
    
    def __str__(self) -> str:
        result = f"{self.name.center(30, '*')}\n"
        for operation in self.ledger:
            result += f"{operation['description'][:23]:<23}{operation['amount']:>7.2f}\n"
        return result + f"Total: {self.get_balance()}"
        
    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def get_balance(self) -> float:
        funds = 0
        for operation in self.ledger:
            funds += operation["amount"]
        return funds
    
    def transfer(self, amount: float, diffrent_category: "Category") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount,"description": f"Transfer to {diffrent_category.name}"})
            diffrent_category.deposit(amount, f"Transfer from {self.name}") 
            return True
        else:
            return False
    
    def check_funds(self, amount: float) -> bool:
        return True if self.get_balance() >= amount else False

def create_spend_chart(categories: list["Category"]) -> str:
    expenses = dict()
    for category in categories:
        expenses[category.name] = sum([operation["amount"] for operation in category.ledger if operation["amount"] < 0])
    
    all_expenses = sum([x for x in expenses.values()])
    expenses = {category: (value / all_expenses) * 100 for category, value in expenses.items()}
    
    print(expenses.keys())
    print(expenses.values())
    
    bar_chart = "Percentage spent by category\n"
    for percent in range(100, -1, -10):
        bar_chart += f"{percent:>3}| {'  '.join(['o' if percentage_spent >= percent else ' ' for percentage_spent in expenses.values()])}  \n"
    
    bar_chart += f"    -{'--'.join(['-' for _ in range(len(expenses))])}--"

    for x in zip_longest(*expenses.keys(), fillvalue=' '):
        bar_chart += f"\n     {'  '.join(x)}  "
    
    return bar_chart

if __name__=="__main__":
    
    # food = Category("Food")
    # food.deposit(1000, "initial deposit")
    # food.withdraw(10.15, "groceries")
    # food.withdraw(15.89, "restaurant and more food for dessert")
    # print(food.get_balance())
    # clothing = Category("Clothing")
    # food.transfer(50, clothing)
    # clothing.withdraw(25.55)
    # clothing.withdraw(100)
    # auto = Category("Auto")
    # auto.deposit(1000, "initial deposit")
    # auto.withdraw(15)

    # print(food)
    # print(clothing)
    # print(auto)
    
    # print(create_spend_chart([food,clothing,auto]))
    
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    print(create_spend_chart([business, food, entertainment]))