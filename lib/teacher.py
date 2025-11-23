#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Teaching basics"]  # Must have at least one item

    def teach(self, student=None, info=None):
        """
        If student and info are provided, teach the student.
        If no info is provided, pick a random item from knowledge and return it.
        """
        if student and info:
            student.learn(info)
        else:
            # Return a random knowledge item if called without arguments
            return random.choice(self.knowledge)
