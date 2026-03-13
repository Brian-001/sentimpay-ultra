class BudgetAgent:

    def __init__(self):

        self.daily_budget = 5.0
        self.spent_today = 0

    def can_spend(self, amount):

        if self.spent_today + amount > self.daily_budget:
            return False

        return True

    def record_spend(self, amount):

        self.spent_today += amount