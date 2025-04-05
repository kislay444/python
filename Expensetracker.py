import json

expenses = []
budgets = {}
filename = "expenses.json"

def save_data():
    data = {"expenses": expenses, "budgets": budgets}
    with open(filename, "w") as f:
        json.dump(data, f)

def load_data():
    global expenses, budgets
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            expenses = data.get("expenses", [])
            budgets = data.get("budgets", {})
    except FileNotFoundError:
        expenses = []
        budgets = {}
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    expenses.append({"amount": amount, "category": category, "description": description})
    save_data()
    print("Expense added.")

def set_budget():
    category = input("Enter category: ")
    amount = float(input("Enter budget amount: "))
    budgets[category] = amount
    save_data()
    print("Budget set.")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
    else:
        for i, e in enumerate(expenses, 1):
            print(f"{i}. {e['category']} - ${e['amount']} - {e['description']}")

def view_budget_status():
    print("Budget Status:")
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    for cat, budget in budgets.items():
        spent = totals.get(cat, 0)
        print(f"{cat}: Spent ${spent} / Budget ${budget}")

load_data()

while True:
    print("\n1. Add Expense")
    print("2. Set Budget")
    print("3. View Expenses")
    print("4. View Budget Status")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        set_budget()
    elif choice == "3":
        view_expenses()
    elif choice == "4":
        view_budget_status()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
