class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []
    def add(self, node):
        self.frontier.append(node)
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.empty():
            print("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier.remove(node)
            return node
class Maze:
    def __init__(self):
        with open("maze.txt") as f:
            contents = f.read()
        if contents.count("A") != 1:
            raise Exception("Problem with A")
        if contents.count("B") != 1:
            raise Exception("Problem with B")
        
        contents = contents.splitlines()
        self.height = len(contents)
        self.weight = max(len(line) for line in contents)

node = Node()