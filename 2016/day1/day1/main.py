from Day1Solution import Day1Solution


def main():

    solution = Day1Solution()
    directions = solution.read_directions()
    solution.travel(solution, directions=directions)
    end_point = solution.determine_distance()

    print(end_point)

if __name__ == "__main__":
    main()
