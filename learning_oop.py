
class Employee:

    raise_amt = 1.05
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # this method does not take class or instance as a first argument instead it can take any
    # general argument. Static method does not work on instance and class

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# learning Inheritenc method. Accessing property of a class to new class with out affecting the
# the inherited class is called Inheritance.


class Developer(Employee):
    raise_amt = 1.10


# emp_1 = Employee('Dharmendra', 'Kumar', 50000)
# emp_2 = Employee('Ripunjoy', 'Gohain', 70000)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)


# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.fullname())

# import datetime
# mydate = datetime.datetime(2020, 2, 23)
# print(Employee.is_workday(mydate))

dev_1 = Developer("Dharmendra", "kumar", 50000)
dev_2 = Developer("Ripunjoy", "Gohain", 60000)
print(dev_1.email)
# print(help(Developer))
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
