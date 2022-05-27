




class Employee:
    def __init__(self, Firstname, Lastname, Salary, shift):
        self.firstname = Firstname
        self.lastname = Lastname
        self.salary = Salary
        self.shift = shift


    def getfullname(self):
        return  f"{self.firstname} {self.lastname}"

    def raiseSAlary(self,amount):
        self.salary = self.salary + amount

class Mechanic(Employee):
    jobtitle="Mechanic"

class Attendant(Employee):
    jobtitle="Attendant"

class Cook(Employee):
    jobtitle="Cook"

class Manager(Employee):
    jobtitle="Manager"


