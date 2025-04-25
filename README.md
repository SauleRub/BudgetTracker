# budget-tracker
📌 BudgetTracker – Personal Expense Analyzer

BudgetTracker is a simple, smart Python tool that helps users track and analyze their personal spending. It loads mock data from JSON, summarizes expenses, breaks down spending by category, filters by month, and exports detailed reports — all directly from the terminal.

🔍 Features
	•	✅ Load and preview expenses
	•	✅ Calculate total and average spending
	•	✅ Analyze spending by category
	•	✅ Filter expenses by month
	•	✅ Export report to .txt and .json formats

🛠️ Technologies Used
	•	Python 
	•	JSON
	•	Faker (to generate test data)
	•	File handling
	•	Clean terminal output

📁 Project Structure
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