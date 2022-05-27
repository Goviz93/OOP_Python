
import unittest
from employee import Employee
from shift import MorningShift


class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):
        e = Employee("Vera","Schmidt","$2000", MorningShift())
        self.assertEqual(e.getfullname(),"Vera Schmidt")

    def test_raiseSAlary(self):
        e = Employee("Vera","Schmidt",2000, MorningShift())
        e.raiseSAlary(125)
        self.assertEqual(e.salary,2125)