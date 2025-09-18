# budget-tracker

# 📊 BudgetTracker – Personal Expense Analyzer

**BudgetTracker** is a smart Python tool that helps users track and analyze their personal spending.  
It loads mock data from JSON, summarizes expenses, breaks them down by category, filters by month, and exports detailed reports — all directly from the terminal.

🔗 [🌐 View Project Demo on Loom](https://www.loom.com/share/be67ee4bfb7d432d88bc3bfeb4c392d4)
---

## 🧠 Core Features

1. **🧾 Generate Expense Data**  
   - Faker-based simulation of 50 fake personal expenses  
   - Fields: Date, Description, Amount, Category

2. **🔍 Load and Preview Expenses**  
   - Loads JSON file  
   - Shows first 5 entries as a quick preview

3. **💰 Total and Average Spending**  
   - Calculates total amount spent  
   - Computes average per expense

4. **📂 Spending by Category**  
   - Summarizes how much was spent on each category (Food, Transport, Entertainment, etc.)

5. **🗓️ Filter by Month**  
   - Filters expenses by month (example: March)  
   - Displays total spending for that month

6. **📤 Export Reports**  
   - `.txt` – Human-readable summary  
   - `.json` – Machine-readable data export

---

## 🛠️ Technologies Used

- Python 🐍  
- Faker (for test data generation)  
- JSON  
- File Handling  
- Terminal CLI (Command Line Interface)

---

## 📁 Project Structure

BudgetTracker/
├── data/
│   └── fake_expenses.json         # Generated test data
├── src/
│   ├── expense_logger.py          # Main analytics logic
│   ├── utils.py                   # (Optional helpers)
│   └── init.py
├── tests/
│   └── test_expense_logger.py     # (Optional tests)
├── generate_fake_data.py          # Generates fake expense data
├── report.txt                     # Exported readable report
├── report.json                    # Exported JSON report
├── requirements.txt               # Python dependencies
└── README.md

---

## 🚀 How to Run the Project

### 🛒 1. Clone the Repository

```bash
git clone https://github.com/SauleRub/BudgetTracker.git
cd BudgetTracker



⸻

🧹 2. Create and Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate

(If you are on Windows, use venv\Scripts\activate)

⸻

📦 3. Install the Required Packages

pip install -r requirements.txt



⸻

✨ 4. Generate Fake Expenses

Run the script to create example expense data:

python generate_fake_data.py

This will create a file inside the data/ folder called fake_expenses.json.

⸻

📊 5. Run the Expense Analyzer

python src/expense_logger.py

You will see:
	•	A preview of your expenses
	•	Total and average spending
	•	Spending breakdown by category
	•	March-only filtered expenses
	•	Exported reports: report.txt and report.json

