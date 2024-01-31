class ExpenseTracker:
    def __init__(self):
        self.expenses = {
            'needs': {'rent': [], 'food': [], 'laundry': [], 'groceries': []},
            'wants': {'apparel': [], 'travel': [], 'etc': []}
        }

    def addSubcategory(self, main_category, subcategory):
        """Add a new subcategory under the specified main category."""
        if main_category in self.expenses and subcategory not in self.expenses[main_category]:
            self.expenses[main_category][subcategory] = []

    # def trackExpenses(self, main_category, subcategory, amount):
    #     """Monitor and record expenses."""
    #     if main_category not in self.expenses:
    #         self.expenses[main_category] = {}
    #     if subcategory not in self.expenses[main_category]:
    #         self.addSubcategory(main_category, subcategory)
    #     self.expenses[main_category][subcategory].append(amount)

    def getExpenseReport(self):
        """Generate reports on user spending."""
        report = {}
        for main_category, subcategories in self.expenses.items():
            report[main_category] = {}
            for subcategory, amounts in subcategories.items():
                report[main_category][subcategory] = {
                    'total': sum(amounts),
                    'transactions': len(amounts),
                    'average': sum(amounts) / len(amounts) if amounts else 0
                }
        return report