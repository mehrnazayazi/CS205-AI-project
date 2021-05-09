n = 4


class Puzzle:
    p = []
    cost = 0

    def set_puzzle(self, p):
        self.p = p

    def set_cost(self, cost):
        self.cost = cost

    def copy_p(self, p):
        for item in self.p:
            p.append(item)

def misplaced_tile_distance(puzzle):
    distance = 0
    for i in range(n * n):
        if puzzle[i] != goal.p[i]:
            distance += 1
    return distance


def manhattan_distance(puzzle):
    i, j, distance = 0
    for item in range(n * n):
        i = item / n # where it is
        j = item % n
        place_i = puzzle.p[item] / n # where it should be
        place_j = puzzle.p[item] % n
        distance += (abs(i - place_i) + abs(j - place_j))
    return distance


if __name__ == '__main__':
    starting_node = Puzzle()
    starting_node.set_puzzle([5, 1, 3, 4, 13, 2, 10, 8, 15, 14, 11, 7, 9, -1, 6, 12])
    starting_node.set_cost(0)
    goal = Puzzle()
    goal.set_puzzle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1])
    seen = []
    unseen = [starting_node]
    path = [starting_node]
    while unseen:
        min_h = 100000000
        node_current = unseen[0]
        # find the node with min h
        for item in unseen:
            h = item.cost + misplaced_tile_distance(item.p)
            if h < min_h:
                node_current = item
                min_h = h
        seen.append(node_current.p)
        path.append(node_current)
        if node_current.p == goal.p:
            for i in path:
                print((i.p))

        blank_position = 0
        i = 0
        for i in range(n*n):
            if node_current.p[i] == -1:
                blank_position = i
                break
        child = Puzzle()
        # move blank one to the right
        if i % n != (n-1):
            child_puzzle = []
            node_current.copy_p(child_puzzle)
            child_puzzle[i] = child_puzzle[i+1]
            child_puzzle[i+1] = -1
            if child_puzzle not in seen:
                child.set_puzzle(child_puzzle)
                child.set_cost(node_current.cost + 1)
                unseen.append(child)
        # move blank one to the left
        if i % n != 0:
            child_puzzle = node_current.p
            child_puzzle[i] = child_puzzle[i-1]
            child_puzzle[i-1] = -1
            if child_puzzle not in seen:
                child.set_puzzle(child_puzzle)
                child.set_cost(node_current.cost + 1)
                unseen.append(child)
        # move blank up
        if i // n != 0:
            child_puzzle = node_current.p
            child_puzzle[i] = child_puzzle[i-n]
            child_puzzle[i-n] = -1
            if child_puzzle not in seen:
                child.set_puzzle(child_puzzle)
                child.set_cost(node_current.cost + 1)
                unseen.append(child)
        # move blank down
        if i // n != n-1:
            print(i/n)
            child_puzzle = node_current.p
            child_puzzle[i] = child_puzzle[i + n]
            child_puzzle[i + n] = -1
            if child_puzzle not in seen:
                child.set_puzzle(child_puzzle)
                child.set_cost(node_current.cost + 1)
                unseen.append(child)




