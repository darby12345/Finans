class PersonalFinanceTracker:
    def __init__(self):
        self.expenses = []
        self.goals = []

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})

    def view_expenses(self):
        if self.expenses:
            print("Expenses:")
            for expense in self.expenses:
                print(f"{expense['category']}: ${expense['amount']}")
        else:
            print("No expenses recorded yet.")

    def set_goal(self, goal, amount):
        self.goals.append({"goal": goal, "amount": amount})

    def view_goals(self):
        if self.goals:
            print("Goals:")
            for goal in self.goals:
                print(f"{goal['goal']}: ${goal['amount']}")
        else:
            print("No goals set yet.")


def main():
    tracker = PersonalFinanceTracker()

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Goal")
        print("4. View Goals")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully.")

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            goal = input("Enter financial goal: ")
            amount = float(input("Enter goal amount: "))
            tracker.set_goal(goal, amount)
            print("Goal set successfully.")

        elif choice == "4":
            tracker.view_goals()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
