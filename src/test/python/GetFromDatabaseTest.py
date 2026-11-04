'''
File: GetFromDatabaseTest.py
Project: DevOps
Author: Dylan Greene
Created: 04/11/2026
Copyright (c) 2026 Dylan Greene
'''

# AI used to generate code for these tests

import unittest
from src.resources.python.backEnd import GetFromDatabase

class TestGetUserId(unittest.TestCase):
    def test_getUserId(self):
        # Test the getUserId function with a valid username
        user_id = GetFromDatabase.getUserId("testuser")
        self.assertIsNotNone(user_id)