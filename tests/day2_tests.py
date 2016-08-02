import unittest

from advent_of_code.day2.Day2Solution import Day2Solution


class TestDay2Solution(unittest.TestCase):

    def setUp(self):
        self.day2solution = Day2Solution()

    def testCorrectAreas(self):

        assert(self.day2solution.calculate_area(2, 3, 4) == 58)
        assert(self.day2solution.calculate_area(1, 1, 10) == 43)

    def testInvalidMeasurements(self):

        try:
            self.day2solution.calculate_area(2, 1, "b")
        except TypeError:
            pass

if __name__ == "__main__":
    unittest.main()
