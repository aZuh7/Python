# Python Object-Oriented Programming


class Employee:
    raise_amount = 1.04

    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


# Class is a blueprint for creating instances

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(Employee.num_of_emps)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# emp_1.apply_raise()
# print(emp_1.pay)


# # emp_1.raise_amount
# # Employee.raise_amount

# Instnce variables contain data that is unique to each instance

#emp_1.first = "Corey"
#emp_1.last = "Schafer"
#emp_1.email = 'Corey.Schaer@company.com'
#emp_1.pay = 60000

#emp_2.first = "Test"
#emp_2.last = "User"
#emp_2.email - 'Test.User@company.com'
#emp_2.pay = 60000


# We want the abililty to perform some action
# can do manually like:
#print('{} {}'.format(emp_1.first, emp_1.last))

# or create a method in our class.
# print(emp_1.fullname())

# print(emp_1.email)
# print(emp_2.email)

# can also run these methods by using the class itself
# emp_1.fullname()
# print(Employee.fullname(emp_1))
