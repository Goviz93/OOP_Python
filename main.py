from employee import Mechanic,Cook,Manager,Attendant
from reports import AccountingReport,StaffingReport, ScheduleReport
from shift import MorningShift, AfternoonShift,NightShift



employees = [

    Manager("Vera","Schmidt","$2000", MorningShift()),
    Attendant("Chuck","Norris","$1800",MorningShift()),
    Attendant("Samantha","Carrington","$1800",AfternoonShift()),
    Cook("Roberto","Jacketti","$2100",MorningShift()),
    Mechanic("Dave","DreiBig","$2200",MorningShift()),
    Mechanic("Tina","River","$2300",MorningShift()),
    Mechanic("Ringo","Rama","$1900",AfternoonShift()),
    Mechanic("Chuck","RAiney","$1800",NightShift()),

]

reports = [
            AccountingReport(employees),
            StaffingReport(employees),
            ScheduleReport(employees),
]

for r in reports:
    r.print_Report()