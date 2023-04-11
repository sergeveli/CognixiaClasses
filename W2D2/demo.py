"""Example"""
class Employee:
    """Classroom example"""
    company = "Cognixia"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary    
    def get_employee_email(self):
        """get employee's email"""
        return f"{self.name.lower()}@{Employee.company.lower()}.com"
    def get_company_domain(self):
        """Get domain name"""
        return f"...@{Employee.company.lower()}.com"
alice = Employee('Alice', 50000)
bob = Employee("Bob", 50000)

print(alice.company, Employee.company)
