import math

coordinateList = []
costList = []
# Node declaration
# Setting boundary as 300x200
class Node:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

# Actions
def moveUp(node):
    newNode = Node(0,0,math.inf)
    if node.x - 1 < 0:
        return False, node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y
        newNode.cost = node.cost + 1
    return True, newNode

def moveDown(node):
    newNode = Node(0,0,math.inf)
    if node.x + 1 > 199:
        return False, node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y
        newNode.cost = node.cost + 1
    return True, newNode

def moveLeft(node):
    newNode = Node(0,0,math.inf)
    if node.y - 1 < 0:
        return False, node
    else:
        newNode.x = node.x
        newNode.y = node.y - 1
        newNode.cost = node.cost + 1
    return True, newNode

def moveRight(node):
    newNode = Node(0,0,math.inf)
    if node.y + 1 > 299:
        return False, node
    else:
        newNode.x = node.x
        newNode.y = node.y + 1
        newNode.cost = node.cost + 1
    return True, newNode

def moveUpLeft(node):
    newNode = Node(0,0,math.inf)
    if node.x - 1 < 0 or node.y - 1 < 0:
        return False, node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y - 1
        newNode.cost = node.cost + math.sqrt(2)
    return True, newNode

def moveUpRight(node):
    newNode = Node(0,0,math.inf)
    if node.x - 1 < 0 or node.y + 1 > 299:
        return False, node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y + 1
        newNode.cost = node.cost + math.sqrt(2)
    return True, newNode

def moveDownLeft(node):
    newNode = Node(0,0,math.inf)
    if node.x + 1 > 199 or node.y - 1 < 0:
        return False, node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y - 1
        newNode.cost = node.cost + math.sqrt(2)
    return True, newNode

def moveDownRight(node):
    newNode = Node(0,0,math.inf)
    if node.x + 1 > 199 or node.y + 1 > 299:
        return False, node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y + 1
        newNode.cost = node.cost + math.sqrt(2)
    return True, newNode

def dijkstra(node):
    coordinateList.append((node.x,node.y))
    costList.append(node.cost)
    while True:
        