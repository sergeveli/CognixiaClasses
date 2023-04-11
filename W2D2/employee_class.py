"""Create a class for employees based on the code you already have and the OOP structure. 
Utilize the 4 pillars of OOP to your advantage."""


class Employee:
    def __init__(self, first_name: str, last_name: str, age: int, birth_year: int):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.age = age
        self.birth_year = birth_year
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}{str(self.birth_year)[-2:]}@company.com"

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_age(self) -> int:
        return self.age

    def get_birth_year(self) -> int:
        return self.birth_year

    def get_email(self) -> str:
        return self.email


"""Here's an explanation of how this class utilizes the 4 pillars of OOP:

Encapsulation: The Employee class encapsulates all the information and functionality related to an employee. This allows the class to be modular and easily maintainable.
Abstraction: The Employee class abstracts away the implementation details of how an employee's information is stored and accessed. This makes it easier to use the Employee class in other parts of the program.
Inheritance: The Employee class does not inherit from any other class, but it could be extended by subclassing if needed.
Polymorphism: The Employee class implements the get_full_name, get_age, get_birth_year, and get_email methods, which are polymorphic in nature. This allows the same interface to be used to access different types of employee information."""
