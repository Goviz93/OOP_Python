

class report:
    def __init__(self, employeeList):
        self._emp_List = employeeList

class AccountingReport(report):
    def print_Report(self):
        print("\nAccounting")
        print("==========")
        for e in self._emp_List:
            print(f"{e.getfullname()}, {e.salary}")

class StaffingReport(report):
    def print_Report(self):
        print("\nStaffing")
        print("==========")
        for e in self._emp_List:
            print(f"{e.getfullname()}, {e.jobtitle}")

class ScheduleReport(report):
    def print_Report(self):
        print("\nSchedule")
        print("==========")
        for e in self._emp_List:
            print(f"{e.getfullname()}, {e.shift.get_shift_info()}")