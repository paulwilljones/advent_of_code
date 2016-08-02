#!/usr/bin/python

import unittest

from advent_of_code.day1.Day1Solution import Day1Solution


class Day1SolutionTests(unittest.TestCase):

    def setUp(self):
        self.day1_solution = None
        self.counter_test_data = {
            "string1": ["(())", 0],
            "string2": ["()()", 0],
            "string3": ["))(((((", 3],
            "string4": ["())", -1],
            "string5": ["))(", -1],
            "string6": [")))", -3],
            "string7": [")())())", -3]
        }

        self.basement_test_data_pass = {
            "string1": ["())", 3]
        }
        self.basement_test_data_fail = {
            "string2": ["(((", 0]
        }

    def test_counter(self):
        for key in self.counter_test_data.keys():
            self.day1_solution = Day1Solution(self.counter_test_data[key][0])
            results = self.day1_solution.counter(['(', ')'])
            floor = results.get('(') - results.get(')')
            assert(floor == self.counter_test_data[key][1])

    def _test_basement(self, test_data):
        for key in test_data.keys():
            self.day1_solution = Day1Solution(test_data[key][0])
            result = self.day1_solution.basement_counter()
            assert(result == test_data[key][1])

    def test_basement_positive(self):
        self._test_basement(self.basement_test_data_pass)

    def test_basement_negative(self):
        with self.assertRaises(AssertionError):
            self._test_basement(self.basement_test_data_fail)


if __name__ == '__main__':
    unittest.main()
