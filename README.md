# OpenLab Python

Collection of Python-related exercises.

## Python basics

**List of exercises**:

1. Convert a string to a list: create a simple Python function that takes a sentence and returns a list of words

2. SpongeBob meme generator: create a Python function that takes a string and returns a SpongeBob-like string. Optional:
you can create a program that uppercases random characters in the word.

3. Reversed string: create a Python function that takes a string and returns its inverse

4. Guess a number: generate a number between 1 and 20 and let the user guess it. Program should guide the user
`Your guess is too low` or `Your guess is too high`.

5. Write a bubble sort sorting algorithm.

6. Mexican wave: create a function that turns a string into a Mexican Wave

**Expected results**:

(1) `'OpenLab is awesome' => ['OpenLab', 'is', 'awesome']`

(2) `'OpenLab is awesome' => 'oPeNlAb iS aWeSoMe'`

(3) `'awesome' => 'emosewa'`

(6) `'hello' => ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']`

## Python classes

1. Create a class called `OpenLab` with the following member variables: (1) list of mentors, (2) list of workshops and
(3) total number of people working here.

2. Now create a class called `Member` which has three member variables: (1) name, (2) email and (3) date of birth (use
`datetime`). This class should also include a method called `compute_age` which returns age of the participant in years.

3. Next, create two classes called `Mentor` and `Participant`.
    
    1. Both `Mentor` and `Participant` classes should inherit from `Member` class
    2. `Mentor` class should have additional properties (1) workshop name and (2) list of programming languages he/she
    knows. In addition to that, there should be a method called `return_mentor_data` which prints email, name and workshop
    name in the console
    3. `Participant` class should have one additional property called `visited_workshops` which is a list of workshops he/she
    visits.
    
4. Place these classes in their respective files. Create one file called `__init__.py` in the project root where you

    1. Create mocks
    2. Have a `def main()` method and an initializer
    
    After completing this, you have your very own Python program!
 
5. Add mocks into `OpenLab` class and think of some methods that would return data in human readable format. (This step
is about you being creative!)
   
6. Optional: you can think of a better architecture for your application, like storing workshop names in constants or
catching incorrect inputs...
 