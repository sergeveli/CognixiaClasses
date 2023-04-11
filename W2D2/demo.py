"""Example"""
class Employee:
    """Classroom example"""
    company = "Cognixia"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


alice = Employee('Alice', 50000)
bob = Employee("Bob", 50000)

print(alice.company, Employee.company)
