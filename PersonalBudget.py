def get_income():
    while True:
        try:
            income = float(input("Enter your total monthly income: $"))
            return income
        except ValueError:
            print("Please enter a valid number for income.")

def get_expenses():
    expenses = {}
    num_expenses = int(input("How many monthly expenses do you have? "))
    
    for i in range(num_expenses):
        expense_name = input(f"Enter expense name {i+1}: ")
        while True:
            try:
                expense_amount = float(input(f"Enter expense amount for {expense_name}: $"))
                expenses[expense_name] = expense_amount
                break
            except ValueError:
                print("Please enter a valid number for expense amount.")
    
    return expenses

def calculate_total_income(income):
    return income

def calculate_total_expenses(expenses):
    return sum(expenses.values())

def calculate_leftover(income, expenses):
    total_income = calculate_total_income(income)
    total_expenses = calculate_total_expenses(expenses)
    
    return total_income - total_expenses

def main():
    print("Welcome to the Personal Budget Calculator!")
    print("------------------------------------------")
    
    income = get_income()
    expenses = get_expenses()
    
    total_income = calculate_total_income(income)
    total_expenses = calculate_total_expenses(expenses)
    leftover = calculate_leftover(income, expenses)
    
    print("\n----- Summary -----")
    print(f"Total Monthly Income: ${total_income:.2f}")
    print(f"Total Monthly Expenses: ${total_expenses:.2f}")
    print(f"Amount Left Over: ${leftover:.2f}")

if __name__ == "__main__":
    main()