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
