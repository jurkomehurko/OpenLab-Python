import datetime

from mentor import Mentor
from participant import Participant
from openlab import OpenLab

# Mentors
peter_dob = datetime.datetime(1996, 8, 16)
peter_lang = ['Java', 'Kotlin', 'Python', 'JavaScript', 'TypeScript', 'C', 'C++', 'Dart', 'PHP']
peter = Mentor('Peter', 'peter@openlab.si', peter_dob, 'AI', peter_lang)

tian_dob = datetime.datetime(2001, 11, 4)
tian_lang = ['C#', 'JavaScript', 'C', 'C++']
tian = Mentor('Tian', 'tian@openlab.si', tian_dob, 'Unity', tian_lang)

mentor_list = [peter, tian]
workshop_list = ['AI', 'Unity']
number_of_employees = len(mentor_list) + 15

# Participants
janez_dob = datetime.datetime(1990, 1, 1)
janez_workshops = ['AI', 'Unity']
janez = Participant('Janez', 'jb@openlab.si', janez_dob, janez_workshops)

openlab = OpenLab(mentor_list, workshop_list, number_of_employees)
openlab.mentors_count()
openlab.workshops()
openlab.total_number_of_employees()
