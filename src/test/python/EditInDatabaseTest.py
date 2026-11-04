'''
File: EditInDatabaseTest.py
Project: DevOps
Author: Dylan Greene
Created: 04/11/2026
Copyright (c) 2026 Dylan Greene
'''

# AI used to generate code for these tests
import unittest
from src.resources.python.backEnd import EditInDatabase

class TestCreateShow(unittest.TestCase):
    def test_createShow(self):
        # Test the createShow function with valid inputs
        result = EditInDatabase.createShow("Test Show", 3, "Test Channel", "Test Creator", 8, 1)
        self.assertTrue(result)

    def test_createShow_invalid_seasons(self):
        # Test the createShow function with invalid seasons input
        result = EditInDatabase.createShow("Test Show", -1, "Test Channel", "Test Creator", 8, 1)
        self.assertFalse(result)

    def test_createShow_invalid_rating(self):
        # Test the createShow function with invalid rating input
        result = EditInDatabase.createShow("Test Show", 3, "Test Channel", "Test Creator", 11, 1)
        self.assertFalse(result)