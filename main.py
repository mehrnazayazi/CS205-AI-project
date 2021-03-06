import numpy as np
import time

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
        # where it is
        i = item / n
        j = item % n
        # where it should be
        place_i = puzzle[item] / n
        place_j = puzzle[item] % n
        if puzzle[item] == -1:
            place_i = n-1
            place_j = n-1
        distance += (abs(i - place_i) + abs(j - place_j))
    return distance


if __name__ == '__main__':
    start_time = 0
    print("please enter 1 for uniform search, Enter 2 for misplaced tile heuristic and enter 3 for manhattan distance")
    hf = int(input())
    print("please enter 1 if you would like to use the default puazzle and enter 2 if you would like to enter a new puzzle")
    p_preference = int(input())
    if p_preference == 1:
        puzzle_initial = [1, 2, 3,4,5,10, 6, 7, 9, 11,-1, 8,13,14,15,12]
    else:
        puzzle_initial = []
        for i in range(n):  # A for loop for row entries
            list = input().split(" ")
            for item in list:
                puzzle_initial.append(int(item))
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
        start_time = time.time()
        min_h = 100000000
        node_current = unseen[0]
        # "Take from the seen list the node node_current with the lowest
        # f(node_current) = g(node_current) + h(node_current)"
        for item in unseen:
            if item in seen:
                unseen.remove(item)
                continue
            # Choose the heuristic based one the input
            if hf == 1:
                h = item.cost
            elif hf == 2:
                h= item.cost + misplaced_tile_distance(item.p)
            else:
                h = item.cost + manhattan_distance(item.p)
            if h < min_h:
                node_current = item
                min_h = h
        seen.append(node_current.p)
        puzzle = []
        # for i in range(n):
        #     row = []
        #     for j in range(n):
        #         row.append(node_current.p[i * n + j])
        #     puzzle.append(row)
        # print(np.array(puzzle))
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
    print("--- %s seconds ---" % (time.time() - start_time))


