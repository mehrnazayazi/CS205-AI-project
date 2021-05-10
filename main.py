import numpy as np

n = 4


class Puzzle:
    def __init__(self, p, cost, parent):
        self.p = p
        self.cost = cost
        self.parent = parent

    def set_puzzle(self, p):
        self.p = p

    def set_cost(self, cost):
        self.cost = cost

    def set_parent(self, parent):
        self.parent = parent

    def copy_p(self, p):
        for member in self.p:
            p.append(member)


def misplaced_tile_distance(puzzle):
    distance = 0
    for i in range(n * n):
        if puzzle[i] != goal.p[i]:
            distance += 1
    return distance


def manhattan_distance(puzzle):
    i, j, distance = 0, 0, 0
    for item in range(n * n):
        i = item / n # where it is
        j = item % n
        place_i = puzzle.p[item] / n # where it should be
        place_j = puzzle.p[item] % n
        distance += (abs(i - place_i) + abs(j - place_j))
    return distance


if __name__ == '__main__':
    puzzle_initial = [1, 2, 3, 4, 5, 6, 7, 8, -1, 10, 11, 12, 9, 13, 14, 15]
    initial_cost = 0
    parent = None
    starting_node = Puzzle(puzzle_initial, initial_cost, parent)
    goal_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1]
    goal_cost = None
    goal_parent = None
    goal = Puzzle(goal_puzzle, goal_cost, goal_parent)
    seen = []
    unseen = [starting_node]
    path = [starting_node]
    while unseen:
        min_h = 100000000
        node_current = unseen[0]
        # "Take from the seen list the node node_current with the lowest
        # f(node_current) = g(node_current) + h(node_current)"
        for item in unseen:
            if item in seen:
                unseen.remove(item)
                continue
            h = item.cost + misplaced_tile_distance(item.p)
            if h < min_h:
                node_current = item
                min_h = h
        seen.append(node_current.p)
        path.append(node_current)
        # "if node_current is node_goal we have found the solution; break"
        if node_current.p == goal.p:
            goal = node_current
            break
        # find the position of blank in the puzzle
        blank_position = 0
        i = 0
        for i in range(n*n):
            if node_current.p[i] == -1:
                blank_position = i
                break
        # "Generate each state node_successor that come after node_current"
        # Move blank one to the right
        if blank_position % n != (n-1):
            child_puzzle = []
            node_current.copy_p(child_puzzle)
            child_puzzle[blank_position] = child_puzzle[blank_position+1]
            child_puzzle[blank_position+1] = -1
            if child_puzzle not in seen:
                child = Puzzle(child_puzzle, node_current.cost+1, node_current)
                unseen.append(child)
        # Move blank one to the left
        if blank_position % n != 0:
            child_puzzle = []
            node_current.copy_p(child_puzzle)
            child_puzzle[blank_position] = child_puzzle[blank_position-1]
            child_puzzle[blank_position-1] = -1
            if child_puzzle not in seen:
                child = Puzzle(child_puzzle, node_current.cost+1, node_current)
                unseen.append(child)
        # move blank up
        if blank_position // n != 0:
            child_puzzle = []
            node_current.copy_p(child_puzzle)
            child_puzzle[blank_position] = child_puzzle[blank_position-n]
            child_puzzle[blank_position-n] = -1
            if child_puzzle not in seen:
                child = Puzzle(child_puzzle, node_current.cost+1, node_current)
                unseen.append(child)
        # Move blank down
        if blank_position // n != n-1:
            child_puzzle = []
            node_current.copy_p(child_puzzle)
            child_puzzle[blank_position] = child_puzzle[blank_position + n]
            child_puzzle[blank_position + n] = -1
            if child_puzzle not in seen:
                child = Puzzle(child_puzzle, node_current.cost+1, node_current)
                unseen.append(child)
        unseen.remove(node_current)

    node = goal
    print("solution")
    path = []
    while node is not None:
        puzzle = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(node.p[i*n+j])
            puzzle.append(row)
        path.append(puzzle)
        node = node.parent
    for i in range(len(path)):
        print(np.array(path.pop()))
        print("---------------------")


