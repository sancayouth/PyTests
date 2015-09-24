# -*- coding: utf-8 -*-
import unittest
from prefix import PrefixCalc


class Tests(unittest.TestCase):

    def setUp(self):
        self.calc = PrefixCalc()

    def test_empty_input(self):
        self.calc.setInput('')
        self.assertEquals('', self.calc.getInput())

    def test_unbalanced_input(self):
        self.assertRaises(ValueError, self.calc.setInput, '+ + 2 2')

    def test_another_unbalanced_input(self):
        self.assertRaises(ValueError, self.calc.setInput, '+ + 2')

    def test_input_equals_str(self):
        self.calc.setInput('+ 2 2')
        self.assertEquals('+ 2 2', self.calc.getInput())

    def test_anoter_input_equals_str(self):
        self.calc.setInput('+ 2 3')
        self.assertEquals('+ 2 3', self.calc.getInput())

    def test_add_operation_equals_6(self):
        self.calc.setInput('+ 3 3')
        self.assertEquals(6.0, self.calc.calculate())

    def test_add_operation_equals_120(self):
        self.calc.setInput('+ 80 40')
        self.assertEquals(120.0, self.calc.calculate())

    def test_result_negative_number(self):
        self.calc.setInput('- 3 7')
        self.assertEquals(-4.0, self.calc.calculate())

    def test_longer_input(self):
        self.calc.setInput('+ - 5 6 7')
        self.assertEquals(6, self.calc.calculate())

    def test_another_longer_input(self):
        self.calc.setInput('+ * 2 3 5')
        self.assertEquals(11, self.calc.calculate())
