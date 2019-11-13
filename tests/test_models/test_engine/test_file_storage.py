#!/usr/bin/python3
"""Unittests for base model class"""


import unittest
from models.engine.file_storage import FileStorage

class TestsFileStorage(unittest.TestCase):

    def test_normal_cases_base_model(self):
        """normal cases"""
        my_object = FileStorage()
        self.assertEqual(my_object.all, my_object.__objects)
