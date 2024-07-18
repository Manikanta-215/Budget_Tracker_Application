import json
from datetime import datetime

# Function to add a transaction (expense or income)
def add_transaction(trans_type, category, amount):
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": trans_type,
        "category": category,
        "amount": amount
    }
    transactions.append(transaction)
    save_transactions()

# Function to save transactions to a JSON file
def save_transactions():
    with open('budget_data.json', 'w') as f:
        json.dump(transactions, f, indent=4)

# Function to calculate remaining budget
def calculate_budget():
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'income')
    total_expenses = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'expense')
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function to analyze expenses by category
def analyze_expenses_by_category():
    categories = {}
    for transaction in transactions:
        if transaction['type'] == 'expense':
            category = transaction['category']
            amount = transaction['amount']
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
    return categories


# Function to load transactions from JSON file
def load_transactions():
    try:
        with open('budget_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Initialize transactions list
transactions = load_transactions()

def main():
    while True:
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses by Category")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_transaction('expense', category, amount)
        elif choice == '2':
            category = input("Enter income source: ")
            amount = float(input("Enter income amount: "))
            add_transaction('income', category, amount)
        elif choice == '3':
            remaining_budget = calculate_budget()
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == '4':
            categories_spending = analyze_expenses_by_category()
            for category, amount in categories_spending.items():
                print(f"{category}: ${amount}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
