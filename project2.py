#Building an Expense Tracking System
#In this project, you will build a simple expense tracking system using only the concepts you have
#learned so far. You will design functions to add, store, analyze, and summarize expenses.


#Part 1: Simulate a Database
#Create a global list called:
#expensesThis list will store all expense entries.
#Each expense should be stored as a dictionary containing: amount, category, description


#Part 2: Add Expense Function
#Create a function:
#add_expense(amount, category, description)
#This function must:
#Validate that amount is greater than 0
#Raise a ValueError if the amount is invalid
#Create a dictionary for the expense
#Append it to the expenses list
#Return the created expense


#Part 3: Calculate Total Expenses
#Creae a function:
#calculate_total_expenses()
#This function must:
#Loop through all expenses
#Calculate the total amount
#Return the total



#Part 4: Calculate Total by Category
#Create a function:
#calculate_total_by_category(category)
#This function must:
#Loop through expenses
#Calculate the total only for the given category
#Return the total


#Part 5: Show All Expenses
#Create a function:
#show_expenses()
#This function must display all stored expenses clearly


#Part 6: Testing Section
#Add a testing section at the bottom of your script that:
#Adds multiple expenses
#Includes at least one invalid expense
#Prints total expenses
#Prints total for a specific category
#Displays all stored expenses


#Final Requirements
#Your solution must:
#Be clean and well structured
#Use readable variable names
#Include comments where necessary to explain your logic
#Make sure to follow best practices writing functions including descriptions.
#Follow proper indentation and formatting
#Avoid unnecessary or duplicated code



# -------------------------------------------------
# Simulated Database
# -------------------------------------------------
 
expenses = []
 
 
# -------------------------------------------------
# Add Expense Function
# -------------------------------------------------
 
def add_expense(amount: float, category: str, description: str) -> dict:
    """
    Add a new expense to the system.
 
    Args:
        amount (float): The expense amount (must be positive).
        category (str): The expense category.
        description (str): Short description of the expense.
 
    Returns:
        dict: The created expense dictionary.
 
    Raises:
        ValueError: If the amount is not greater than 0.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
 
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
 
    expenses.append(expense)
    return expense
 
 
# -------------------------------------------------
# Calculate Total Expenses
# -------------------------------------------------
 
def calculate_total_expenses() -> float:
    """
    Calculate the total of all expenses.
 
    Returns:
        float: Total amount of all expenses.
    """
    total = 0
 
    for expense in expenses:
        total += expense["amount"]
 
    return total
 
 
# -------------------------------------------------
# Calculate Total by Category
# -------------------------------------------------
 
def calculate_total_by_category(category: str) -> float:
    """
    Calculate total expenses for a specific category.
 
    Args:
        category (str): The category to filter by.
 
    Returns:
        float: Total amount for that category.
    """
    total = 0
 
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]
 
    return total
 
 
# -------------------------------------------------
# Show All Expenses
# -------------------------------------------------
 
def show_expenses() -> None:
    """
    Display all stored expenses.
 
    Returns:
        None
    """
    if not expenses:
        print("No expenses recorded.")
        return
 
    print("\nAll Expenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"{expense['description']} : ${expense['amount']}"
        )
 
 
# -------------------------------------------------
# Testing Section
# -------------------------------------------------
 
def run_tests() -> None:
    """
    Execute example expense scenarios.
    """
    try:
        add_expense(50, "Food", "Groceries")
        add_expense(20, "Transport", "Taxi")
        add_expense(100, "Food", "Restaurant")
        add_expense(0, "Entertainment", "Cinema")  # Invalid example
 
    except ValueError as error:
        print("Error:", error)
 
    print("\nTotal Expenses:", calculate_total_expenses())
    print("Total Food Expenses:", calculate_total_by_category("Food"))
 
    show_expenses()
 
 
if __name__ == "__main__":
    run_tests()