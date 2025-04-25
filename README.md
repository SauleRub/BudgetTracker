# budget-tracker
# 📊 BudgetTracker – Personal Expense Analyzer

**BudgetTracker** is a smart Python tool that helps users track and analyze their personal spending.  
It loads mock data from JSON, summarizes expenses, breaks them down by category, filters by month, and exports detailed reports — all directly from the terminal.

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
   - Summarizes how much was spent on each category (Food, Transport, etc.)

5. **🗓️ Filter by Month**  
   - Filters expenses by month (e.g., March)  
   - Displays total for that month only

6. **📤 Export Reports**  
   - `.txt` – Human-readable summary  
   - `.json` – Machine-readable for further use

---

## 🛠️ Technologies Used

- Python 
- Faker (for test data)  
- JSON  
- File Handling  
- Terminal CLI (Command Line Interface)

---

## 📁 Project Structure

BudgetTracker/
├── data/
│   └── fake_expenses.json       # Generated mock data
├── src/
│   ├── expense_logger.py        # Core analysis logic
├── generate_fake_data.py        # Script to generate data
├── report.txt                   # Exported report
├── report.json                  # Exported report (JSON)
├── requirements.txt             # Python dependencies
└── README.md
