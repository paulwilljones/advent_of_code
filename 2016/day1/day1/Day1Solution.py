from fn import recur


class Day1Solution(object):

    def __init__(self):
        self.movements = [0, 0]
        self.current_direction = 0

    @staticmethod
    def read_directions():

        with open('../files/input.txt', 'r') as directions_file:
            directions = directions_file.read().replace(' ', '').split(',')

        return directions

    def turn(self, next_direction):
        if next_direction == "L":
            self.current_direction += -1
        elif next_direction == "R":
            self.current_direction += 1
        if self.current_direction > 3:
            self.current_direction = 0
        elif self.current_direction < 0:
            self.current_direction = 3

    def update_movements(self, distance_to_travel):
        try:
            self.movements[self.current_direction] += int(distance_to_travel)
        except IndexError:
            self.movements[self.current_direction - 2] -= int(distance_to_travel)

    def determine_distance(self):
        return sum([abs(n) for n in self.movements])

    @recur.tco
    def travel(self, directions):
        if len(directions):
            next_move = directions.pop(0)
            self.turn(next_move[0])
            distance_to_travel = next_move[1:]
            self.update_movements(distance_to_travel)
            return True, (self, directions, )
        else:
            return False, self.movements
