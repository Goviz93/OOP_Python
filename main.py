from employee import Mechanic,Cook,Manager,Attendant
from reports import AccountingReport,StaffingReport




employees = [

    Manager("Vera","Schmidt","$2000"),
    Attendant("Chuck","Norris","$1800"),
    Attendant("Samantha","Carrington","$1800"),
    Cook("Roberto","Jacketti","$2100"),
    Mechanic("Dave","DreiBig","$2200"),
    Mechanic("Tina","River","$2300"),
    Mechanic("Ringo","Rama","$1900"),
    Mechanic("Chuck","RAiney","$1800"),

]

Acc_Repo = AccountingReport(employees)
Staff_Repo = StaffingReport(employees)
Acc_Repo.print_Report()
Staff_Repo.print_Report()