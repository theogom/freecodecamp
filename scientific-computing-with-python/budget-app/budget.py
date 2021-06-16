from typing import Dict, List


class Category:
    """
    A class representing a budget category with a money balance
    It has a ledger to keep track of transactions made
    which can be deposit or withdrawal
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the name and the ledger of the category
        """
        self.name: str = name
        self.ledger: List[Dict] = []

    def __str__(self) -> str:
        """
        String representation of the category printing
        the category name and listing all transactions in the ledger
        """
        string = f'{self.name:{"*"}^30}'
        total = 0.0

        for item in self.ledger:
            description = item['description'][:23]
            padding = 30 - len(description)
            amount = f'{item["amount"]:>{padding}.2f}'[:padding + 7]
            total += float(amount)
            string = '\n'.join((string, description + amount))

        string = '\n'.join((string, f'Total: {total}'))

        return string

    def get_balance(self):
        """
        Get the current balance of the budget category
        based on deposits and withdrawals in the ledger
        """
        return sum([object['amount'] for object in self.ledger])

    def check_funds(self, amount: float):
        """
        Check if there are sufficient funds
        in the balance for the given amount
        """
        return amount <= self.get_balance()

    def deposit(self, amount: float, description: str = ''):
        """
        Make a deposit
        """
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount: float, description: str = ''):
        """
        Make a withdrawal
        """
        # Insufficient funds
        if not self.check_funds(amount):
            return False

        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def transfer(self, amount: float, category: 'Category'):
        """
        Make a transaction from the current category to the given category
        """
        # Insufficient funds
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True


def create_spend_chart(categories: List[Category]):
    """
    Create a bar chart representing the percentage spent
    for each category
    """
    title = 'Percentage spent by category'

    # 2D array (or matrix) representation of the chart
    # in which element are characters
    chart_array = []

    # Maximum category length for left padding
    max_cat_len = 0

    # Chart represent the percentage of withdrawals made
    withdrawals = []
    for category in categories:
        withdrawals.append(
            sum([
                (float(transaction['amount']) if
                 float(transaction['amount']) < 0 else 0)
                for transaction in category.ledger
            ])
        )
        cat_len = len(category.name)
        max_cat_len = max(max_cat_len, cat_len)

    # Total amount spent
    total = sum(withdrawals)

    # y-axis percentage scale
    scale = [f'{i * 10:>3}|' for i in range(10, -1, -1)] \
        + ['    ' for _ in range(max_cat_len + 1)]
    chart_array.append(scale)

    # Separator between each bar
    separator = list(' ' * 11 + '-' + ' ' * max_cat_len)
    chart_array.append(separator)

    for index, category in enumerate(categories):
        percentage = int(withdrawals[index] / total * 100 // 10 * 10)
        chart_array.append(
            list(
                f'{category.name[::-1]:>{max_cat_len}}'
                '-'
                f'{(percentage // 10 + 1) * "o":<11}'[::-1]
            )
        )
        chart_array.extend((separator, separator))

    # Create the string representing the chart
    # by going through the matrix line by line
    chart = title
    x_length = len(categories) * 3 + 2
    y_length = len(chart_array[0])
    for j in range(y_length):
        string = ''.join([chart_array[i][j] for i in range(x_length)])
        chart = '\n'.join((chart, string))

    return chart
