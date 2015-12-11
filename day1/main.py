import collections


def main():
    with open('input.txt') as f:
        read_data = f.read()
        results = counter(['(', ')'], read_data)

    print "Floor: {}".format(results.get('(') - results.get(')'))

    return


def counter(chars_to_count, to_parse):
    char_counters = {}
    for char_to_count in chars_to_count:
        char_counter = collections.Counter(to_parse)
        char_counters.update({char_to_count: char_counter.get(char_to_count, 0)})

    return char_counters

if __name__ == "__main__":
    main()
