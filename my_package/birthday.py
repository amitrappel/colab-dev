from datetime import datetime

class BirthDay:
    def __init__(year, month, day):
        self.bday = datetime(year, month, day)     

    def get_weekday():
        return self.bday.weekday()
    
    def get_age(self)
        return datetime.now() - self.bday
