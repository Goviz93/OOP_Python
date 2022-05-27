import datetime


class Shift:
    def get_shift_info(self):
        return (f"{self.StartTime:%H:%M} to {self.EndTime:%H:%M}")


class MorningShift(Shift):
    StartTime = datetime.time(8,00)
    EndTime = datetime.time(14,00)

class AfternoonShift(Shift):
    StartTime = datetime.time(12,00)
    EndTime = datetime.time(20,00)

class NightShift(Shift):
    StartTime = datetime.time(14,00)
    EndTime = datetime.time(22,00)