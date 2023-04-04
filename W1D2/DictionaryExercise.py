# Prompt the user for their name, age, and years coding
name = input("What is your name? ")
age = int(input("What is your age? "))
years_coding = int(input("How many years have you been coding? "))

# Prompt the user for their first three programming languages
prog_langs_first = tuple(input(
    "Enter your first three programming languages, separated by commas: ").split(", "))

# Prompt the user for their three favorite programming languages
prog_langs_fav = input(
    "Enter your three favorite programming languages, separated by commas: ").split(", ")

# Create a set that is an intersection of their first programming languages and their favorite programming languages
prog_langs_intersection = set(prog_langs_first) & set(prog_langs_fav)

# Create a dictionary with the collected data
data = {
    'name': name,
    'age': age,
    'years_coding': years_coding,
    'prog_langs_first': prog_langs_first,
    'prog_langs_fav': prog_langs_fav,
    'prog_langs_intersection': prog_langs_intersection
}

# Format a print statement to print the relevant data to the console
print(f"Name: {data['name']}\nAge: {data['age']}\nYears Coding: {data['years_coding']}\n"
      f"First Programming Languages: {data['prog_langs_first']}\n"
      f"Favorite Programming Languages: {data['prog_langs_fav']}\n"
      f"Intersection of First and Favorite Programming Languages: {data['prog_langs_intersection']}")
