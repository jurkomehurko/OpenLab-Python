from member import Member


class Participant(Member):
    def __init__(self, name, email, date_of_birth, visited_workshops):
        super().__init__(name, email, date_of_birth)
        self.visited_workshops = visited_workshops
