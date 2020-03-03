import math
from Environment import *

nodeList = []
parentList = []
childList = []
costList = []


# Node declaration
# Setting boundary as 300x200
class Node:
    def __init__(self, x, y, cost, parent):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent


# Actions
def moveUp(node):
    newNode = Node(0, 0, math.inf, (0, 0))
    if node.x - 1 < 0:
        return False, node
    if check_Obstacle(node.x,node.y):
        return False,node

    else:
        newNode.x = node.x - 1
        newNode.y = node.y
        newNode.cost = node.cost + 1
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveDown(node):
    newNode = Node(0, 0, math.inf, (0, 0))
    if node.x + 1 > 199:
        return False, node
    if check_Obstacle(node.x,node.y):
        return False,node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y
        newNode.cost = node.cost + 1
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveLeft(node):
    newNode = Node(0, 0, math.inf, (0, 0))
    if node.y - 1 < 0:
        return False, node
    if check_Obstacle(node.x,node.y):
        return False,node
    else:
        newNode.x = node.x
        newNode.y = node.y - 1
        newNode.cost = node.cost + 1
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveRight(node):
    newNode = Node(0, 0, math.inf, (0, 0))
    if node.y + 1 > 299:
        return False, node
    if check_Obstacle(node.x,node.y):
        return False,node
    else:
        newNode.x = node.x
        newNode.y = node.y + 1
        newNode.cost = node.cost + 1
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveUpLeft(node):
    newNode = Node(0, 0, math.inf, (0, 0))
    if node.x - 1 < 0 or node.y - 1 < 0:
        return False, node
    if check_Obstacle(node.x,node.y):
        return False,node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y - 1
        newNode.cost = node.cost + math.sqrt(2)
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveUpRight(node):
    newNode = Node(0, 0, math.inf, (0, 0))
    if node.x - 1 < 0 or node.y + 1 > 299:
        return False, node
    if check_Obstacle(node.x,node.y):
        return False,node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y + 1
        newNode.cost = node.cost + math.sqrt(2)
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveDownLeft(node):
    newNode = Node(0, 0, math.inf, (0, 0))
    if node.x + 1 > 199 or node.y - 1 < 0:
        return False, node
    if check_Obstacle(node.x,node.y):
        return False,node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y - 1
        newNode.cost = node.cost + math.sqrt(2)
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveDownRight(node):
    newNode = Node(0, 0, math.inf, (0, 0))
    if node.x + 1 > 199 or node.y + 1 > 299:
        return False, node
    if check_Obstacle(node.x,node.y):
        return False,node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y + 1
        newNode.cost = node.cost + math.sqrt(2)
        newNode.parent = (node.x, node.y)
    return True, newNode


def redundantNode(coordinate):
    if coordinate in childList:
        return False
    return True


def addNode(node):
    if check_Obstacle(node.x,node.y):
        return
    else:
        if redundantNode((node.x, node.y)):
            parentList.append(node.parent)
            childList.append((node.x, node.y))
            nodeList.append(node)
            costList.append(node.cost)
        else:
            index = childList.index((node.x, node.y))
            if nodeList[index].cost > node.cost:
                nodeList[index].cost = node.cost
                costList[index] = node.cost
                nodeList[index].parent = node.parent


def backTracking(parent, child):
    # starting from the last parent node
    parentnode = parent[len(parent) - 1]
    childnode = child[len(child) - 1]
    nodePath = []
    nodePath.append(childnode)
    nodePath.append(parentnode)
    while parentnode != (0,0):
        if parentnode in child:
            index = child.index(parentnode)
            parentnode = parent[index]
            nodePath.append(parentnode)
    nodePath = nodePath[::-1]
    return nodePath

def goalReached(node, goal):
    if (node.x, node.y) == goal:
        addNode(node)
        print('goal reached')
        print('Cost took to reach the goal is: ' + str(node.cost))
        return True
    return False


def dijkstra(node, goal):
    count = 0
    if goalReached(node, goal):
        return
    if check_Obstacle(node.x,node.y) and check_Obstacle(goal[0],goal[1]):
        return
    else:

        nodeList.append(node)
        parentList.append((0, 0))
        childList.append((node.x, node.y))
        costList.append(0)
        while True:
            status, newNode = moveLeft(node)
            if goalReached(newNode, goal):
                break
            else:
                if status:
                    addNode(newNode)
            status, newNode = moveRight(node)
            if goalReached(newNode, goal):
                break
            else:
                if status:
                    addNode(newNode)
            status, newNode = moveUp(node)
            if goalReached(newNode, goal):
                break
            else:
                if status:
                    addNode(newNode)
            status, newNode = moveDown(node)
            if goalReached(newNode, goal):
                break
            else:
                if status:
                    addNode(newNode)
            status, newNode = moveUpLeft(node)
            if goalReached(newNode, goal):
                break
            else:
                if status:
                    addNode(newNode)
            status, newNode = moveUpRight(node)
            if goalReached(newNode, goal):
                break
            else:
                if status:
                    addNode(newNode)
            status, newNode = moveDownLeft(node)
            if goalReached(newNode, goal):
                break
            else:
                if status:
                    addNode(newNode)
            status, newNode = moveDownRight(node)
            if goalReached(newNode, goal):
                break
            else:
                if status:
                    addNode(newNode)
            # nodeList.pop(0)
            count += 1
            node = nodeList[count]
            print(count)


# Passing inputs
simulation = False
node = Node(5, 15, 0, (0, 0))
goal = (95, 105)
dijkstra(node, goal)
nodepath = backTracking(parentList,childList)
simulation = True

for node in nodeList:
    draw_Explored_Nodes(node.x,node.y)

for pixel in nodepath:
    draw_Optimal_Nodes(pixel[0],pixel[1])

while simulation:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
        
        
        