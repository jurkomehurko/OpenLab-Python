class OpenLab:
    def __init__(self, mentor_list, workshops_list, number_of_employees):
        self.mentor_list = mentor_list
        self.workshop_list = workshops_list
        self.number_of_employees = number_of_employees

    def mentors_count(self):
        print('OpenLab has ' + str(len(self.mentor_list)) + ' mentors')

    def workshops(self):
        print('We offer ' + str(len(self.workshop_list)) + ' workshops: ' + str(', '.join(self.workshop_list)))

    def total_number_of_employees(self):
        print('OpenLab has a team of ' + str(self.number_of_employees) + ' people!')
