"""This program prompts the user for the number of employees they want to add, 
then loops through each employee and prompts for their name, age, and birth year. 
It formats the name, generates the email, and saves the data to a file. 
Finally, it prints each employee's information in a formatted string."""

import datetime
import os

def get_input(prompt, data_type=str, min_value=None, max_value=None):
    """Define a function to get user input with error handling"""
    while True:
        try:
            user_input = data_type(input(prompt))
            if min_value is not None and user_input < min_value:
                raise ValueError(f"Input must be at least {min_value}")
            if max_value is not None and user_input > max_value:
                raise ValueError(f"Input must be at most {max_value}")
            return user_input
        except ValueError as error:
            print(f"Invalid input: {error}")

def format_name(name):
    """Define a function to format the name"""
    first_name, last_name = name.split()
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{first_name} {last_name}"

def generate_email(name, birth_year):
    """Define a function to generate the email"""
    first_name, last_name = name.split()
    last_name += str(birth_year)[-2:]
    return f"{first_name.lower()}.{last_name.lower()}@company.com"

# Define the main function to capture employee data


def main():
    """Get the number of employees"""
    num_employees = get_input(
        "How many employees will you add? ", int, min_value=1, max_value=10)

    # Create a list to hold employee dictionaries
    employees = []

    # Loop for each employee and record their information
    for i in range(num_employees):
        # Get the employee's name and split it into first and last
        name = get_input(f"Enter the name of employee #{i+1}: ")
        name = format_name(name)

        # Get the employee's age and birth year
        birth_year = get_input(
            f"Enter the birth year of employee #{i+1}: ", int, min_value=1900, 
            max_value=datetime.datetime.now().year)
        age = get_input(
            f"Enter the age of employee #{i+1}: ", int, min_value=0)

        # Generate the email
        email = generate_email(name, birth_year)

        # Add the employee to the list
        employee = {"Name": name, "Age": age,
                    "Birth Year": birth_year, "Email": email}
        employees.append(employee)

    # Print each employee's information in a formatted string
    for employee in employees:
        print(
            f"Name: {employee['Name']}\nAge: {employee['Age']}\nBirth Year: {employee['Birth Year']}\nEmail: {employee['Email']}\n")

    # Save the employee data to a file
    filename = "employee_data.txt"
    if not os.path.exists(filename):
        with open(filename, "w", encoding="UTF-8") as file:
            file.write("Name,Age,Birth Year,Email\n")
    with open(filename, "a", encoding="UTF-8") as file:
        for employee in employees:
            file.write(
                f"{employee['Name']},{employee['Age']},{employee['Birth Year']},{employee['Email']}\n")


# Call the main function
if __name__ == "__main__":
    main()
