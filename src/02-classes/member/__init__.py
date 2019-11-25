from datetime import date


class Member:
    def __init__(self, name, email, date_of_birth):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth

    def compute_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        print(str(self.name) + ' is ' + str(age) + ' years old')
