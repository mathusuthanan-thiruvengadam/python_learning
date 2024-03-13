class xdate:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.date = d
    
    def __repr__(self):
        return f"{self.year}/{self.month}/{self.date}"
    
    def __add__(self, days):
        new_date = self.date + days
        new_month = self.month
        new_year = self.year
        
        # Adjusting the date if it exceeds the number of days in the month
        while new_date > self.days_in_month(new_year, new_month):
            new_date -= self.days_in_month(new_year, new_month)
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1
        
        return xdate(new_year, new_month, new_date)

    def __sub__(self, days):
        new_date = self.date - days
        new_month = self.month
        new_year = self.year
        
        # Adjusting the date if it becomes negative
        while new_date <= 0:
            new_month -= 1
            if new_month == 0:
                new_month = 12
                new_year -= 1
            new_date += self.days_in_month(new_year, new_month)
        
        return xdate(new_year, new_month, new_date)

    @staticmethod
    def days_in_month(year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            else:
                return 28
        else:
            raise ValueError("Invalid month")
        

