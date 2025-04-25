import json

def load_expenses(filepath="data/fake_expenses.json"):
    try:
        with open(filepath, "r") as file:
            expenses = json.load(file)
        return expenses
    except FileNotFoundError:
        print("Expense file not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []

def print_summary(expenses):
    print(f"Loaded {len(expenses)} expenses:")
    for expense in expenses[:5]:  
        print(f" - {expense['date']}: {expense['description']} - ${expense['amount']} ({expense['category']})")
def get_total_spent(expenses):
    return sum(expense["amount"] for expense in expenses)

def get_average_spent(expenses):
    if not expenses:
        return 0
    return get_total_spent(expenses) / len(expenses)

from collections import defaultdict

def get_spending_by_category(expenses):
    category_totals = defaultdict(float)
    for expense in expenses:
        category = expense["category"]
        category_totals[category] += expense["amount"]
    return category_totals

def filter_by_month(expenses, month: int):
    return [e for e in expenses if int(e["date"].split("-")[1]) == month]

def export_report_txt(total, average, category_totals, filename="report.txt"):
    with open(filename, "w") as f:
        f.write(f"Total spent: ${total:.2f}\n")
        f.write(f"Average per expense: ${average:.2f}\n\n")
        f.write("Spending by category:\n")
        for category, amount in category_totals.items():
            f.write(f" - {category}: ${amount:.2f}\n")
    print(f"\n Report saved to {filename}")

def export_report_json(total, average, category_totals, filename="report.json"):
    import json
    report = {
        "total": round(total, 2),
        "average": round(average, 2),
        "spending_by_category": category_totals
    }
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
    print(f" Report saved to {filename}")

if __name__ == "__main__":
    expenses = load_expenses()
    print_summary(expenses)
    total = get_total_spent(expenses)
    average = get_average_spent(expenses)
    print(f"\n Total spent: ${total:.2f}")
    print(f" Average per expense: ${average:.2f}")
    
    category_totals = get_spending_by_category(expenses)
    print("\n Spending by category:")
    for category, amount in category_totals.items():
        print(f" - {category}: ${amount:.2f}")

    march_expenses = filter_by_month(expenses, 3)
    march_total = get_total_spent(march_expenses)
    print(f"\n Total spent in March: ${march_total:.2f}")

    export_report_txt(total, average, category_totals)
    export_report_json(total, average, category_totals)
