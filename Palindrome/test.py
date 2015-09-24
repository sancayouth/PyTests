# -*- coding: utf-8 -*-
import unittest
from palindrome import Palindrome


class Tests(unittest.TestCase):

    def test_palindrome_word(self):
        pal = Palindrome()
        result = pal.parseword('neuquen')
        self.assertTrue(result)

    def test_palindrome_with_spaces(self):
        pal = Palindrome()
        result = pal.parseword('La ruta natural')
        self.assertTrue(result)

    def test_not_palindrome_word(self):
        pal = Palindrome()
        result = pal.parseword('solamente')
        self.assertFalse(result)

    def test_palindrome_number(self):
        pal = Palindrome()
        result = pal.parseword('12321')
        self.assertTrue(result)