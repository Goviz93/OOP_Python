




class Employee:
    def __init__(self, Firstname, Lastname, Salary):
        self.firstname = Firstname
        self.lastname = Lastname
        self.salary = Salary

    def getfullname(self):
        return  f"{self.firstname} {self.lastname}"

class Mechanic(Employee):
    jobtitle="Mechanic"

class Attendant(Employee):
    jobtitle="Attendant"

class Cook(Employee):
    jobtitle="Cook"

class Manager(Employee):
    jobtitle="Manager"


