import unittest
from unittest.mock import patch
import sys
import app

class test_App(unittest.TestCase):
    """ Class to test the app"""

    def test_input_number(self):
        """Check input number"""
        testargs = ["main", "139"]
        with patch.object(sys, 'argv', testargs):
            result = app.main()
            self.assertTrue(result)

    def test_no_matches(self):
        """Check no matches"""
        testargs = ["main", "0"]
        with patch.object(sys, 'argv', testargs):
            result = app.main()
            self.assertFalse(result)

    def test_no_input(self):
        """Check no input"""
        testargs = ["main"]
        with patch.object(sys, 'argv', testargs):
            setup = app.main()
            self.assertFalse(setup)

    def test_input_string(self):
        """Check input string"""
        testargs = ["main", "twenty"]
        with patch.object(sys, 'argv', testargs):
            setup = app.main()
            self.assertFalse(setup)

    def test_input_list(self):
        """Check input list"""
        testargs = ["main", []]
        with patch.object(sys, 'argv', testargs):
            setup = app.main()
            self.assertFalse(setup)
