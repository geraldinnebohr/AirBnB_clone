#!/usr/bin/python3
"""Unittests for base model class"""


import unittest
from models.place import Place
from datetime import datetime
from uuid import UUID
from models import storage


class TestsBaseModel(unittest.TestCase):
    """
    class for unit testing
    """
    def setUp(self):
        """set initial"""
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def test_normal_cases_place(self):
        """normal cases"""
        my_object = Place()
        my_object.name = "Holbiland"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "Holbiland")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "Place")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

if __name__ == "__main__":
    unittest.main()
