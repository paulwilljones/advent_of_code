from Day2Solution import Day2Solution


def main():

    solution = Day2Solution()
    total_area = 0
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip().split("x")
            area = solution.calculate_area(length=int(
                line[0]), width=int(line[1]), height=int(line[2]))
            total_area += area

    print total_area

    return


if __name__ == "__main__":
    main()
