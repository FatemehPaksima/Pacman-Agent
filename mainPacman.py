import random
from queue import Queue

actions = { "L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
# تابع محیط
def environment_action(action):
    global AgentPosition, matrix

    newPos = (
        AgentPosition[0] + actions[action][0],
        AgentPosition[1] + actions[action][1],
    )

    if matrix[newPos[0]][newPos[1]] == "*":
        status = "W"
        game_history[newPos[0]][newPos[1]] = "*"

    elif matrix[newPos[0]][newPos[1]] == "f":
        status = "F"
        game_history[newPos[0]][newPos[1]] = "f"
        AgentPosition = newPos
    elif matrix[newPos[0]][newPos[1]] == "-" or matrix[AgentPosition[0]][AgentPosition[1]] == "a":
        status = "E"
        game_history[newPos[0]][newPos[1]] = "-"
        AgentPosition = newPos
    else:
        status = "NOTFOUND"
    return [AgentPosition, status]

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

def add_nodes_to_frontier(parent):
    for action in actions:
        state = (
            AgentPosition[0] + actions[action][0],
            AgentPosition[1] + actions[action][1],
        )
        if not game_frontier.contains_state(state) and game_history[state[0]][state[1]] == '?':
            game_frontier.add(Node(state, parent, action))

class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def is_empty(self):
        return len(self.frontier) == 0

    def contains_state(self, state):
        return any(
            node.state[0] == state[0] and node.state[1] == state[1]
            for node in self.frontier
        )

    def remove(self):
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node

game_frontier = QueueFrontier()
# تابع عامل
def game_agent():
    global AgentPosition

    start = Node(AgentPosition, parent=None, action=None)
    add_nodes_to_frontier(start)

    while True:

        node = game_frontier.remove()
        AgentPosition = node.parent.state
        percept = environment_action(node.action)

        if percept[1] == "F":
            return node
        elif percept[1] == "E":
            add_nodes_to_frontier(node)

def read_file(input_file):
    global AgentPosition, matrix, game_history

    with open(input_file, "r") as file:
        lines = file.readlines()

    dimensions = tuple(map(int, lines[0].split(",")))

    AgentPosition = tuple(map(int, lines[1].split(",")))
    matrix = []

    game_history = [["?" for i in range(dimensions[1])] for i in range(dimensions[0])]
    game_history[AgentPosition[0]][AgentPosition[1]] = "-"

    for line in lines[3:]:
        matrix.append(list(line.strip()))



def food_path(food_node):
    node = food_node
    path = []
    directions = {"U": 1, "R": 2, "D": 3, "L": 4}
    length = 0
    while node.parent is not None:
        length = length + 1
        path.append(node.state)
        path.append(directions[node.action])
        node = node.parent
    path.append(node.state)
    path.reverse()
    return path, length

def game_output(food_node):
    path, length = food_path(food_node)
    return path[0], path[-1], length, path

def set_random(m, n):
    global AgentPosition, matrix, game_history

    food_pos = (random.randint(1, m - 2), random.randint(1, n - 2))

    AgentPosition = (random.randint(1, m - 2), random.randint(1, n - 2))

    while food_pos == AgentPosition:
        AgentPosition = (random.randint(1, m - 2), random.randint(1, n - 2))

    matrix = [["-" for i in range(n)] for i in range(m)]

    game_history = [["?" for i in range(n)] for i in range(m)]
    game_history[AgentPosition[0]][AgentPosition[1]] = "-"

    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                matrix[i][j] = "*"
            elif (i, j) == food_pos:
                matrix[i][j] = "f"
            elif (i, j) == AgentPosition:
                matrix[i][j] = "a"
            elif random.random() < min((m - 2), (n - 2)) * 0.03:
                matrix[i][j] = "*"

def game_history_output():
    global game_history
    for m in game_history:
        print(m)

read_file("input1.txt")
s, f, l, p = game_output(game_agent())
print(s, f, l, p, sep="\n")
game_history_output()