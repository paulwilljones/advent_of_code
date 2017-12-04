import collections


class Day1Solution(object):

    def __init__(self, to_parse):
        self.to_parse = to_parse

    def counter(self, chars_to_count):
        char_counters = {}
        for char_to_count in chars_to_count:
            char_counter = collections.Counter(self.to_parse)
            char_counters.update(
                {char_to_count: char_counter.get(char_to_count, 0)})

        return char_counters

    def basement_counter(self):
        floor_counter, floor_pos = (0, 0)
        for char in self.to_parse:
            if char == '(':
                floor_counter += 1
            elif char == ')':
                floor_counter -= 1

            floor_pos += 1
            if floor_counter == -1:
                break

        assert(floor_counter != len(self.to_parse))

        return floor_pos


def main():
    with open('input.txt') as f:
        read_data = f.read()
        solution = Day1Solution(read_data)
        results = solution.counter(['(', ')'])
        basement_position = solution.basement_counter()

    print "Floor: {}".format(results.get('(') - results.get(')'))
    print "Basement entered after {} floors".format(basement_position)

    return


if __name__ == "__main__":
    main()
