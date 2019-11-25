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

OpenLab.mentor_list = [peter, tian]
OpenLab.workshop_list = ['AI', 'Unity']
OpenLab.number_of_employees = len(OpenLab.mentor_list)

# Participants
janez_dob = datetime.datetime(1990, 1, 1)
janez_workshops = ['AI', 'Unity']
janez = Participant('Janez', 'jb@openlab.si', janez_dob, janez_workshops)

OpenLab.mentor_list[0].return_mentor_data()
janez.compute_age()
tian.compute_age()
print('Number of employees in OpenLab: ' + str(OpenLab.number_of_employees))