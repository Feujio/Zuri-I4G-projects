#!/usr/bin/env python3

from random import randint

class Student:
    """Blueprint for student entity
    """
    @staticmethod
    def input_type_checking(an_obj, a_type, err_message):
        """An independent method to check the type of this class' attributes

        Args:
            an_obj (Any): a value
            a_type (Any): Python built-in classes
            err_message (string): Error message

        Raises:
            ValueError: A message.

        Returns:
            Any: an_obj
        """
        if not isinstance(an_obj, a_type):
            raise ValueError(err_message, an_obj)
        else:
            return an_obj

    def __init__(self, name, age, tracks, score):
        """Constructor

        Args:
            name (str): student's name
            age (int): student's age
            tracks (list): list of tacks the student is enrolled
            score (float): student's score
        """
        self.name = self.input_type_checking(name, str, "You did not provide a valid string value.")
        self.age = self.input_type_checking(age, int, "Age must be an integer value.")
        if isinstance(tracks, list) and ((len (tracks) and isinstance(tracks[0], str) or not len(tracks))):
            self.tracks = tracks
        else:
            self.tracks = self.input_type_checking(tracks, str, "Tracks must be a string or a list of strings.")

        self.score = self.input_type_checking(score, float, "Score must be a number value.")


    def change_name(self, new_name):
        """Change student's name

        Args:
            new_name (string): new name of the student
        """
        if not isinstance(new_name, str):
            raise ValueError("You did not provide a valid string value.", new_name)
        else:
            self.name = new_name


    def change_age(self, new_age):
        """Change student's age

        Args:
            new_age (int): new age of the student
        """
        if not isinstance(new_age, int):
            raise ValueError("Age must be an integer value.")


    def add_track(self, item):
        """Add a new item to student's tracks

        Args:
            item (string): a new track the student follows
        """
        self.tracks.append(item)

    def get_score(self):
        """Returns student's score
        """
        return self.score

    # We can create students with a lot of configuration
    @classmethod
    def student_full_time_fullstack(cls, name, age, score):
        """Alternative constructor for fullstack students on full time ZURI&I4G program

        Args:
            name (str): student's name
            age (int): student's age
            score (ffloat): student's score
        Returns:
            Student : An instance of Student class
        """
        return cls(name, age, ["Fullstack development", "Devops"], score)

    @staticmethod
    def begin_id():
        """An independant method for creating the first charcaters of the student ID
        """
        return f'STU{randint(0, 11000)}'

    def student_id(self):
        """Create the student's ID

        Returns:
            str: student's ID
        """
        return self.begin_id() + self.name


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()