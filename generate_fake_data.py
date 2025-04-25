import json
import random
from faker import Faker
from datetime import datetime

fake = Faker()

CATEGORIES = ["Food", "Transport", "Entertainment", "Utilities", "Healthcare", "Other"]

def generate_fake_expense():
    return {
        "date": fake.date_between(start_date='-3M', end_date='today').strftime("%Y-%m-%d"),
        "description": fake.sentence(nb_words=3),
        "amount": round(random.uniform(5.0, 200.0), 2),
        "category": random.choice(CATEGORIES)
    }

def generate_expenses(n=50):
    return [generate_fake_expense() for _ in range(n)]

if __name__ == "__main__":
    expenses = generate_expenses(50)
    with open("data/fake_expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)
    print("50 fake expenses saved to data/fake_expenses.json")