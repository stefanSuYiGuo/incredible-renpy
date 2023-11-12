init python:
    class Calendar(object):
        def __init__(self, Hours, Minutes, Days, Day, Months, Month, WeekDays, MonthDays):
            self.Hours = Hours
            self.Minutes = Minutes
            self.Days = Days
            self.Day = Day
            self.Months = Months
            self.Month = Month
            self.WeekDays = WeekDays
            self.MonthDays = MonthDays

        @property
        def Output(self):
            return self.WeekDays[self.Day] + " " + self.Months[self.Month] + " " + str(self.Days) + " " + str(self.Hours).zfill(2) + ":" + str(self.Minutes).zfill(2)

        def AddTime(self, hours):
            self.Hours += hours
            if Hours > 23:
                self.Hours -= 24
                self.Day += 1
                self.Days += 1
            if self.Day > 6:
                self.Day = 0
            if self.Days > self.MonthDays[self.Month]:
                self.Month += 1
                self.Days = 0
            if self.Month > 11:
                self.Month = 0