from member import Member


class Mentor(Member):
    def __init__(self, name, email, date_of_birth, workshop_name, languages):
        super().__init__(name, email, date_of_birth)
        self.workshop_name = workshop_name
        self.languages = languages

    def return_mentor_data(self):
        print('Mentor ' + str(self.name) + ', email: ' + str(self.email) + '. Workshop: ' + str(self.workshop_name))
