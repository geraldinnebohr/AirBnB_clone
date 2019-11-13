#!/usr/bin/python3
"""Unittests for user class"""


import unittest
from models.user import User
from datetime import datetime
from uuid import UUID
from models import storage


class TestsUser(unittest.TestCase):

    def test_normal_cases_user(self):
        """normal cases"""
        my_object = User()
        my_object.name = "Holbiland"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "Holbiland")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "User")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

if __name__ == "__main__":
    unittest.main()
