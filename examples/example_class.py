#Example for Class and functions
# define a class
class Employee:
    # define a property
    id = 0
    name = ''
    company_name = ''

    def __init__(self, id=None, name=None):
        if id != None:
            self.id = id
        if name != None:
            self.name = name
        self.company_name = 'CapeStart Pvt Ltd'

    def get_uppercase_name(self):
        return self.name.upper()
    
    def get_lowecase_name(self):
        return self.name.lower()    


def print_employee_details(employee):
    if employee != None:
        print(f"Employee Id: {employee.id}")
        print(f"Employee Name: {employee.name}")
        print(f"Employee Name (in Capital): {employee.get_uppercase_name()}")
        print(f"Company Name: {employee.company_name}")
    else:
        print("Data not found (deleted/NotCreated)")

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access property using employee1
employee1.id = 1001
employee1.name = "John"

# access properties using employee2
employee2.id = 1002
employee2.name = "Bob"
employee2.company_name = 'Branch of CapeStart'

employee3 = Employee(1003, "Jack")

print_employee_details(employee1)
print_employee_details(employee2)
print_employee_details(employee3)

#Updating name of Employee1
employee1.name = "Johny"

#Updating name of Employee2
employee2.name = "Boby"

print_employee_details(employee1)
print_employee_details(employee2)
print_employee_details(employee3)

employee1 = None
employee2 = None
employee3 = None

print_employee_details(employee1)
print_employee_details(employee2)
print_employee_details(employee3)