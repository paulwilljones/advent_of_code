import unittest
from day1.day1_solution import Day1Solution


class Day1SolutionTests(unittest.TestCase):

    def setUp(self):
        self.day1_solution = None
        self.test_data = {
            "string1": ["(())", 0],
            "string2": ["()()", 0],
            "string3": ["))(((((", 3],
            "string4": ["())", -1],
            "string5": ["))(", -1],
            "string6": [")))", -3],
            "string7": [")())())", -3]
        }

    def test_values(self):
        for key in self.test_data.keys():
            self.day1_solution = Day1Solution(self.test_data[key][0])
            results = self.day1_solution.counter(['(', ')'])
            floor = results.get('(') - results.get(')')
            assert(floor == self.test_data[key][1])

if __name__ == '__main__':
    unittest.main()
