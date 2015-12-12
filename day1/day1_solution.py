import collections


class Day1Solution(object):

    def __init__(self, to_parse):
        self.to_parse = to_parse

    def counter(self, chars_to_count):
        char_counters = {}
        for char_to_count in chars_to_count:
            char_counter = collections.Counter(self.to_parse)
            char_counters.update({char_to_count: char_counter.get(char_to_count, 0)})

        return char_counters


def main():
    with open('input.txt') as f:
        read_data = f.read()
        solution = Day1Solution(read_data)
        results = solution.counter(['(', ')'])

    print "Floor: {}".format(results.get('(') - results.get(')'))

    return


if __name__ == "__main__":
    main()
