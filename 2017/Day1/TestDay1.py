#!/usr/bin/env python3

from Day1 import Day1
import unittest


class TestDay1(unittest.TestCase):

    def setUp(self):
        self.day1 = Day1.Day1()

    def test_create_class(self):
        self.assertIsInstance(self.day1, Day1.Day1)

    def test_duplicates(self):
        input = [1, 1, 2, 3, 4, 4, 5]

        duplicates = self.day1.duplicates(input)
        sum = self.day1.sum_duplicates(duplicates)

        self.assertEqual([1, 4], duplicates)
        self.assertEqual(5, sum)

    def test_recursive_duplicates(self):
        input = [1, 1, 2, 2]

        duplicates = self.day1.with_trampoline(self.day1.recursive_duplicates)
        found_duplicates = duplicates([], input + [1])

        self.assertEqual([1, 2], found_duplicates)
        self.assertEqual(3, self.day1.sum_duplicates(found_duplicates))

    def test_recursive_duplicates_multiple(self):
        input = [1, 1, 1, 1]

        duplicates = self.day1.with_trampoline(self.day1.recursive_duplicates)
        found_duplicates = duplicates([], input + [1])

        self.assertEqual([1, 1, 1, 1], found_duplicates)
        self.assertEqual(4, self.day1.sum_duplicates(found_duplicates))

    def test_recursive_first_last_match(self):
        input = [9, 1, 2, 1, 2, 1, 2, 9]

        duplicates = self.day1.with_trampoline(self.day1.recursive_duplicates)
        found_duplicates = duplicates([], input + [9])

        self.assertEqual([9], found_duplicates)
        self.assertEqual(9, self.day1.sum_duplicates(found_duplicates))

    def test_recursive_no_matches(self):
        input = [1, 2, 3, 4]

        duplicates = self.day1.with_trampoline(self.day1.recursive_duplicates)
        found_duplicates = duplicates([], input)

        self.assertEqual([], found_duplicates)
        self.assertEqual(0, self.day1.sum_duplicates(found_duplicates))

    def test_duplicate_circular(self):
        input = [1, 2, 1, 2]

        duplicates = self.day1.duplicate_circular(input)
        sum = self.day1.sum_duplicates(duplicates)

        self.assertEqual(6, sum)

if __name__ == "__main__":
    unittest.main()
