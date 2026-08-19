class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"[:7]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate total spent and percentages
    total_spent = 0
    category_spent = []

    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spent.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in category_spent]

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    # Add the horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Add the category names vertically
    max_name_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_name_length) for category in categories]

    for i in range(max_name_length):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip("\n")
