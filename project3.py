#Building Mini Banking System
#In this project, you will build a simple mini banking system using only the concepts you have learned 
#so far. You will design functions to create accounts, manage balances, perform transactions, and display
#account summaries.


#Part 1: Simulate a Database
#Create a global list called:
#accounts This list will store all bank accounts.
#Each account should be stored as a dictionary containing: name, balance, transactions
#The transactions field must be a list. Each transaction should be stored as a dictionary containing:
#  type and amount


#Part 2: Add Expense Function
#Create a function:
#create_account(name, initial_balance)
#This function must:
#Validate that the initial balance is not negative
#Raise a ValueError if the balance is invalid
#Prevent duplicate account names
#Create a dictionary for the account
#Append it to the accounts list
#Return the created account


#Part 3: Deposit Function
#Create a function:
#deposit(name, amount)
#This function must:
#Validate that the amount is greater than 0
#Raise a ValueError if the amount is invalid
#Find the correct account
#Increase the balance
#Add a transaction record with type "Deposit"
#Return the updated balance


#Part 4: Withdraw Function
#Create a function:
#withdraw(name, amount)
#This function must:
#Validate that the amount is greater than 0
#Raise a ValueError if the amount is invalid
#Find the correct account
#Ensure sufficient balance before withdrawing
#Raise a ValueError if funds are insufficient
#Decrease the balance
#Add a transaction record with type "Withdrawal"
#Return the updated balance


#Part 5: Show Accout Summary
#Create a function:
#show_account(name)
#This function must:
#Display the account name
#Display the current balance
#Display all transactions clearly


#Part 6: Testing Section
#Add a testing section at the bottom of your script that:
#Creates at least one account
#Performs multiple deposits
#Performs multiple withdrawals
#Attempts an overdraft
#Attempts creating a duplicate account
#Displays the account summary


#Final Requiremens
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
 
accounts = []
 
 
# -------------------------------------------------
# Helper Function: Find Account
# -------------------------------------------------
 
def find_account(name: str):
    """
    Find an account by name.
 
    Args:
        name (str): Account holder name.
 
    Returns:
        dict: Account dictionary if found.
        None: If account does not exist.
    """
    for account in accounts:
        if account["name"].lower() == name.lower():
            return account
    return None
 
 
# -------------------------------------------------
# Create Account
# -------------------------------------------------
 
def create_account(name: str, initial_balance: float):
    """
    Create a new bank account.
 
    Args:
        name (str): Account holder name.
        initial_balance (float): Starting balance.
 
    Returns:
        dict: Created account dictionary.
 
    Raises:
        ValueError: If balance is negative or account exists.
    """
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")
 
    if find_account(name):
        raise ValueError("Account with this name already exists.")
 
    account = {
        "name": name,
        "balance": initial_balance,
        "transactions": []
    }
 
    accounts.append(account)
    return account
 
 
# -------------------------------------------------
# Deposit
# -------------------------------------------------
 
def deposit(name: str, amount: float):
    """
    Deposit money into an account.
 
    Args:
        name (str): Account holder name.
        amount (float): Amount to deposit.
 
    Returns:
        float: Updated balance.
 
    Raises:
        ValueError: If amount is invalid or account not found.
    """
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than 0.")
 
    account = find_account(name)
 
    if not account:
        raise ValueError("Account not found.")
 
    account["balance"] += amount
 
    account["transactions"].append({
        "type": "Deposit",
        "amount": amount
    })
 
    return account["balance"]
 
 
# -------------------------------------------------
# Withdraw
# -------------------------------------------------
 
def withdraw(name: str, amount: float):
    """
    Withdraw money from an account.
 
    Args:
        name (str): Account holder name.
        amount (float): Amount to withdraw.
 
    Returns:
        float: Updated balance.
 
    Raises:
        ValueError: If insufficient funds or invalid amount.
    """
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than 0.")
 
    account = find_account(name)
 
    if not account:
        raise ValueError("Account not found.")
 
    if amount > account["balance"]:
        raise ValueError("Insufficient funds.")
 
    account["balance"] -= amount
 
    account["transactions"].append({
        "type": "Withdrawal",
        "amount": amount
    })
 
    return account["balance"]
 
 
# -------------------------------------------------
# Show Account Summary
# -------------------------------------------------
 
def show_account(name: str):
    """
    Display account summary including transactions.
 
    Args:
        name (str): Account holder name.
    """
    account = find_account(name)
 
    if not account:
        print("Account not found.")
        return
 
    print(f"\nAccount Summary for {account['name']}")
    print(f"Current Balance: ${account['balance']}")
 
    print("Transactions:")
    if not account["transactions"]:
        print("No transactions yet.")
    else:
        for transaction in account["transactions"]:
            print(f"- {transaction['type']} : ${transaction['amount']}")
 
 
# -------------------------------------------------
# Testing Section
# -------------------------------------------------
 
def run_tests():
    try:
        create_account("Baraa", 1000)
        deposit("Baraa", 200)
        withdraw("Baraa", 150)
        withdraw("Baraa", 2000)  # Overdraft test
 
    except ValueError as error:
        print("Error:", error)
 
    show_account("Baraa")
 
 
run_tests()