# write a python script to capture user input for an Employee. 
# Record the employee's name (split the name into first and last, make sure the first letter of both is capitalized and the rest of the letters are lowercase), 
# record the employee's age (parse the age information to an int, 
# record the employee's birth year), 
# generate the employee's email (concatenate the first and last names with a ".", add the last two digits of thier birth year to the last name, add @company.com to the end) 
# and finally print results to the screen.

name = input("What is your name? ")
age = input("How old are you? ")
profession = input("What is your profession? ")

print(f"Your name is {name}, you are {age} years old, and your profession is {profession}.")


name = input("Enter Employee's full name: ")
age = input("Enter Employee's age: ")

# Split the name into first and last, capitalize the first letter of both, and lowercase the rest of the letters
first_name, last_name = name.split()
first_name = first_name.capitalize()
last_name = last_name.capitalize()

# Parse the age information to an int and calculate the birth year
age = int(age)
birth_year = 2023 - age

# Generate the email address
email = f'{first_name.lower()}.{last_name.lower()}{str(birth_year)[-2:]}@company.com'

# Print the results
print('Employee Name:', first_name, last_name)
print('Employee Age:', age)
print('Employee Birth Year:', birth_year)
print('Employee Email:', email)


# Here's how the script works:

# The script prompts the user to enter the Employee's name and age using the input() function.
# The script splits the name into first and last names using the split() method and capitalizes the first letter of each name and lowercase the rest of the letters.
# The script parses the age information to an integer using the int() function and calculates the birth year based on the current year(2023).
# The script generates the email address by concatenating the first and last names with a ".", adding the last two digits of the birth year to the last name, and adding "@company.com" to the end.
# Finally, the script prints out the Employee's name, age, birth year, and email address to the screen using the print() function.
