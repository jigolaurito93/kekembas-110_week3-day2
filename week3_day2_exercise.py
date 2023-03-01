# Create an Employee class that sets an employee's first name, last name, job title, salary, and email. 
# The Employee class should have a class attribute for the raise amount set to 5% (1.05). 
# Create a method that will apply the raise to an employee's salary.

class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, title, salary):
        self.first_name = first
        self.last_name = last 
        self._job_title = title
        self.salary = salary
        self.email = first.lower() + '.' + last.lower() + '@company.org'

    def full_name(self):
        return self.first_name.title() + ' ' + self.last_name.title()
    
    def apply_raise(self):
        self.salary *= Employee.raise_amount
        print(f"Congrats {self.first_name}, you have received a raise and your new salary is ${self.salary:.2f}")

employee_1 = Employee('John', 'Wick', 'Manager', 50000)
employee_2 = Employee('Ronda', 'Rousey', 'Supervisor', 35000)

# Create two more classes that inherit from the Employee class. One for Sales and one for Development. Both of these classes will have the same attributes as the Employee.

# For the Sales employees, add a phone number attribute on instantiation using the super method.
# Create a method on the Sales class that will Send a Follow Up Email. It should take in a customer name and "send" aka print a 
# formatted email "Dear customer, Thank you for your interest in our product. 
# Please let me know if you have any questions. My email is email or my phone number is phone number. Thanks, full name"
# Create a method on the Development class called code that will print out "full name is writing code".

class Sales(Employee):
    
    def __init__(self, first, last, title, salary, phone):
        super().__init__(first, last, title, salary)
        self.phone = phone

    def follow_up_email(self, customer_name):
        self.customer_name = customer_name
        print(f"Dear {customer_name}, Thank you for your interest in our product.")
        print(f"Please let me know if you have any questions. My email is {self.email} or phone number is {self.phone}. Thanks, {self.full_name()}")

class Development(Employee):

    def __init__(self, first, last, title, salary):
        self.first_name = first
        self.last_name = last 
        self._job_title = title
        self.salary = salary
        self.email = first.lower() + '.' + last.lower() + '@company.org'
    
    def code(self):
        print(f"{self.full_name()} is writing code.")


# Create an instance of a Sales Employee with a salary of $50,000.
# Send follow up emails to "Mike O'Neil" and "Hannah Stern"
# Give the employee a raise and print the salary

print("=" * 150)
tony = Sales('Tony', 'Stark', 'Sales Manager', 50000, '(571)-382-4025')
tony.follow_up_email("Mike O'neal")
print("=" * 150)
tony.follow_up_email('Sarah Stern')
print("=" * 150)
tony.apply_raise()

# Create an instance of a Development Employee with a salary of $100,000
# Write some code with this employee
# Give the employee a raise and print the salary

tina = Development('Tina', 'Turner', 'Development Anaylist', 100000 )
tina.code()
tina.apply_raise()

