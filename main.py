class Ball:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color

class Stick:
    def __init__(self, length):
        self.length = length
        self.balls = []

    def add_ball(self, color):
        self.balls.append(Ball(color))

    def is_full(self):
        return len(self.balls) == self.length

    def __eq__(self, other):
        if len(self.balls) != len(other):
            return False
        same = True
        for i in range(len(self.balls)):
            if self.balls[i].color != other[i]:
                same = False
        return same

class Tower:
    def __init__(self):
        self.sticks = [Stick(length) for length in [4, 3, 2, 1]]
        self.sticks[0].add_ball("teal")
        self.sticks[0].add_ball("yellow")
        self.sticks[0].add_ball("blue")
        self.sticks[0].add_ball("red")

    def move_ball(self, stick1_index, stick2_index):

        stick1 = self.sticks[stick1_index]
        stick2 = self.sticks[stick2_index]
        ball = stick1.balls.pop()
        stick2.balls.append(ball)


    def can_move_ball(self, stick1_index, stick2_index):
        return stick2_index != stick1_index and\
            (len(self.sticks[stick1_index].balls) > 0 and not self.sticks[stick2_index].is_full())

    def valid_moves(self):
        valid_moves_list = []
        for i in range(len(self.sticks)):
            for j in range(len(self.sticks)):
                if self.can_move_ball(i, j):
                    valid_moves_list.append((i, j))
        return valid_moves_list


    def check_valid(self):
        cond1 = self.sticks[0] == ["red", "yellow"]
        cond2 = self.sticks[1] == ["teal", "blue"]
        return cond1 and cond2

    def check_valid_sequence(self, moves_list):
        for move in moves_list:
            self.move_ball(move[0], move[1])
        return self.check_valid()


def BFS():
    # 1. Populate frontier
    frontier = [[valid_move] for valid_move in Tower().valid_moves()]

    while len(frontier) > 0:
        moves_list = frontier.pop(0)
        new_tower = Tower()
        if new_tower.check_valid_sequence(moves_list):
            print(moves_list)
            exit(0)
        if len(moves_list) < 8:
            valid_moves_lst = new_tower.valid_moves()
            for valid_move in valid_moves_lst:
                new_tower_list = moves_list[:]
                new_tower_list.append(valid_move)
                frontier.append(new_tower_list)

if __name__ == "__main__":


    # Manual
    # Set-up problem
    tower_manual = Tower()

    tower_manual.move_ball(0, 3)
    tower_manual.move_ball(0, 2)
    tower_manual.move_ball(0, 2)
    tower_manual.move_ball(0, 1)
    tower_manual.move_ball(3, 0)
    tower_manual.move_ball(2, 0)
    tower_manual.move_ball(2, 1)
    print(tower_manual.check_valid())

    # BFS
    BFS()

