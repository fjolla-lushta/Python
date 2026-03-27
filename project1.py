
#In this project, you will build a small user registration system using only the concepts you have
#learned so far. You must create all validation logic yourself and properly structure the system using
#functions, lists, dictionaries, loops, and exception handling.


#Part 1: Simulate a Database
# Create two global lists:
#registered_users list will store successfully registered users.
#failed_registrations list will store information about failed registration attempts.


#Part 2: Create Validation Functions
#You must create the following three functions:
#validate_name(name)
#The name must contain at least 3 characters.
#Return True if the name is valid, otherwise return False.
#validate_email(email)
#The email must contain both "@" and ".".
#Return True if the email format is valid, otherwise return False.
#validate_password(password)
#The password must meet all of the following conditions:
#At least 8 characters long
#Contains at least one uppercase letter
#Contains at least one digit
#Return True if the password is valid, otherwise return False.

#Part 3: Create a Main Validation Function
#Create an orchestrator function called validate_user_data(name, email, password)
#his function must:
#Call the three validation functions you created
#Raise a ValueError with a clear and descriptive message if any validation fails
#Return True if all validations pass successfully


#Part 4: Create the Registration Function
##Create a function called create_user_account(name, email, password)
#This function must:
#Call validate_user_data() to validate the inputs.
#Check whether the email already exists in the registered_users list.
#If a duplicate email is found, raise a ValueError.
#If validation passes and the email is not duplicated:
#Create a dictionary containing name, email, password, and a status set to "active".
#Append the dictionary to registered_users.
#Return the created user dictionary.
#If any error occurs during validation or duplicate checking:
#Catch the ValueError.
#Store a dictionary inside failed_registrations containing the email and the error message.
#Return None.


#Part 5: Testing Your Implementation
#After completing your solution, add a simple testing section at the bottom of your script.
#Test the following cases:
#A valid registration
#A duplicate email
#An invalid name
#An invalid email
#A weak password
#For each case:
#Call create_user_account()
#Print the result
#Print the final contents of registered_users
#Print the final contents of failed_registrations
#The goal is to clearly demonstrate how your system behaves in both successful and failed scenarios.


#Final Requirements
#Your solution must:
#Be clean and well structured
#Use readable variable names
#Include comments where necessary to explain your logic
#Make sure to follow best practices writing functions including descriptions.
#Follow proper indentation and formatting
#Avoid unnecessary or duplicated code



# -------------------------------------------------------------------
# Simulated Database
# -------------------------------------------------------------------
 
registered_users = []
failed_registrations = []
 
 
# -------------------------------------------------------------------
# Validation Functions
# -------------------------------------------------------------------
 
def validate_name(name: str) -> bool:
    """
    Validate that the name contains at least 3 characters.
 
    Args:
        name (str): The user's name.
 
    Returns:
        bool: True if valid, otherwise False.
    """
    return len(name) >= 3
 
 
def validate_email(email: str) -> bool:
    """
    Validate that the email contains both '@' and '.'.
 
    Args:
        email (str): The user's email address.
 
    Returns:
        bool: True if valid, otherwise False.
    """
    return "@" in email and "." in email
 
 
def validate_password(password: str) -> bool:
    """
    Validate the password strength.
 
    Rules:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one digit
 
    Args:
        password (str): The user's password.
 
    Returns:
        bool: True if valid, otherwise False.
    """
    if len(password) < 8:
        return False
 
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
 
    return has_uppercase and has_digit
 
 
# -------------------------------------------------------------------
# Orchestrator Validation Function
# -------------------------------------------------------------------
 
def validate_user_data(name: str, email: str, password: str) -> bool:
    """
    Validate all user inputs.
 
    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.
 
    Returns:
        bool: True if all validations pass.
 
    Raises:
        ValueError: If any validation rule fails.
    """
    if not validate_name(name):
        raise ValueError("Name must contain at least 3 characters.")
 
    if not validate_email(email):
        raise ValueError("Email must contain '@' and '.'.")
 
    if not validate_password(password):
        raise ValueError(
            "Password must be at least 8 characters long and "
            "contain one uppercase letter and one digit."
        )
 
    return True
 
 
# -------------------------------------------------------------------
# Registration Function
# -------------------------------------------------------------------
 
def create_user_account(name: str, email: str, password: str):
    """
    Create a new user account after validation.
 
    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.
 
    Returns:
        dict: User dictionary if registration succeeds.
        None: If registration fails.
 
    Raises:
        ValueError: Internally raised during validation or duplicate checks.
    """
    try:
        validate_user_data(name, email, password)
 
        if any(user["email"] == email for user in registered_users):
            raise ValueError("An account with this email already exists.")
 
        user_record = {
            "name": name,
            "email": email,
            "password": password,
            "status": "active",
        }
 
        registered_users.append(user_record)
        return user_record
 
    except ValueError as error:
        failed_registrations.append(
            {"email": email, "error": str(error)}
        )
        return None
 
 
# -------------------------------------------------------------------
# Testing Section
# -------------------------------------------------------------------
 
def run_tests():
    """
    Execute sample registration scenarios.
 
    Returns:
        None
    """
    test_cases = [
        ("Baraa", "baraa@email.com", "Password1"),
        ("AnotherUser", "baraa@email.com", "Password1"),
        ("Al", "al@email.com", "Password1"),
        ("Sarah", "sarah@email.com", "weakpass"),
    ]
 
    for index, (name, email, password) in enumerate(test_cases, start=1):
        print(f"\nTest {index}")
        result = create_user_account(name, email, password)
 
        if result:
            print("Registration successful:", result)
        else:
            print("Registration failed.")
 
    print("\nFinal Registered Users:")
    print(registered_users)
 
    print("\nFailed Registrations:")
    print(failed_registrations)
 
 
 
run_tests()
