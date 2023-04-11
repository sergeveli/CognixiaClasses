"""Here's a program that captures user input for an Employee, 
stores the data in a list of dictionaries, and saves it to a file. 
It also includes a module for handling integer user input 
and a main script that tests the functions in the module. 
This program uses list comprehension to get a list of employees under 30, 
and it uses filter and map to get a list of emails for employees over 30."""

import yaml

def get_int_input(prompt, within_range=None):
    """
    Prompts the user to enter an integer value and returns it.

    Args:
        prompt (str): The prompt to display to the user.
        min_val (int, optional): The minimum allowed value. Defaults to None.
        max_val (int, optional): The maximum allowed value. Defaults to None.

    Returns:
        int: The integer value entered by the user.

    Raises:
        ValueError: If user does not enter a valid int value or if the value is outside the range.
    """
    while True:
        try:
            value = int(input(prompt))
            if within_range is not None and (value < within_range[0] or value > within_range[1]):
                raise ValueError(
                    f"Value must be between {within_range[0]} and {within_range[1]}")
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    """
    A function that prompts the user to input employee information, creates a list of employees,
    and writes the employee data to a file. The function utilizes the `get_int_input` function from
    the `input_handler` module to handle user input and error handling. It also uses list comp
    and the `filter` and `map` functions to create a separate list of employees categorized by age.

    Parameters:
        None

    Returns:
        None
    """
    emps = []
    max_emps = 5

    while True:
        num_emps = get_int_input(
            "How many employees would you like to add? ", within_range=(1, max_emps))
        if len(emps) + num_emps <= max_emps:
            break
        else:
            print(
                f"Error: Only {max_emps - len(emps)} employees can be added.")

    for i in range(num_emps):
        print(f"Employee {i+1}")
        first_name = input("Enter first name: ").capitalize()
        last_name = input("Enter last name: ").capitalize()
        age = get_int_input("Enter age: ")
        birth_year = get_int_input("Enter birth year: ")
        email = f"{first_name.lower()}.{last_name.lower()}{str(birth_year)[-2:]}@company.com"
        emp = {
            "first": first_name,
            "last": last_name,
            "age": age,
            "birth_year": birth_year,
            "email": email
        }
        emps.append(emp)
        with open("employees.yaml", "w", encoding="UTF-8") as _f1:
            yaml.dump(emps, _f1)

    with open("employees.txt", "a", encoding="UTF-8") as _f:
        for _ in emps:
            _f.write(
                f"{_['first']} {_['last']} {_['age']} {_['birth_year']} {_['email']}\n")

    print("Employees:")
    for _ in emps:
        print(
            f"{_['first']} {_['last']}, age {_['age']}, email: {_['email']}")

    # Use list comprehension to get employees under 30
    young_emps = [
        emp for emp in emps if emp['age'] < 30]
    print("Employees Under 30:")
    for _ in young_emps:
        print(f"{_['first']} {_['last']}")

    # Use filter and map to get emails for employees over 30
    old_emp_emails = list(map(lambda emp: emp['email'], filter(lambda emp: emp['age'] >= 30, emps)))
    print("Emails for Employees Over 30:")
    for email in old_emp_emails:
        print(email)

if __name__ == "__main__":
    main()
