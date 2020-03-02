import math

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
    newNode = Node(0,0,math.inf,(0,0))
    if node.x - 1 < 0:
        return False, node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y
        newNode.cost = node.cost + 1
        newNode.parent = (node.x, node.y)
    return True, newNode

def moveDown(node):
    newNode = Node(0,0,math.inf,(0,0))
    if node.x + 1 > 199:
        return False, node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y
        newNode.cost = node.cost + 1
        newNode.parent = (node.x, node.y)
    return True, newNode

def moveLeft(node):
    newNode = Node(0,0,math.inf,(0,0))
    if node.y - 1 < 0:
        return False, node
    else:
        newNode.x = node.x
        newNode.y = node.y - 1
        newNode.cost = node.cost + 1
        newNode.parent = (node.x, node.y)
    return True, newNode

def moveRight(node):
    newNode = Node(0,0,math.inf,(0,0))
    if node.y + 1 > 299:
        return False, node
    else:
        newNode.x = node.x
        newNode.y = node.y + 1
        newNode.cost = node.cost + 1
        newNode.parent = (node.x, node.y)
    return True, newNode

def moveUpLeft(node):
    newNode = Node(0,0,math.inf,(0,0))
    if node.x - 1 < 0 or node.y - 1 < 0:
        return False, node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y - 1
        newNode.cost = node.cost + math.sqrt(2)
        newNode.parent = (node.x, node.y)
    return True, newNode

def moveUpRight(node):
    newNode = Node(0,0,math.inf,(0,0))
    if node.x - 1 < 0 or node.y + 1 > 299:
        return False, node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y + 1
        newNode.cost = node.cost + math.sqrt(2)
        newNode.parent = (node.x, node.y)
    return True, newNode

def moveDownLeft(node):
    newNode = Node(0,0,math.inf,(0,0))
    if node.x + 1 > 199 or node.y - 1 < 0:
        return False, node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y - 1
        newNode.cost = node.cost + math.sqrt(2)
        newNode.parent = (node.x, node.y)
    return True, newNode

def moveDownRight(node):
    newNode = Node(0,0,math.inf,(0,0))
    if node.x + 1 > 199 or node.y + 1 > 299:
        return False, node
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
    if redundantNode((node.x,node.y)):
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

# def backtracking(parent, child):
    
def goalReached(node,goal):
    if (node.x, node.y) == goal:
        print('goal reached')
        print('Cost took to reach the goal is: ' + str(node.cost))
        return True
    return False

def dijkstra(node, goal):
    count = 0
    if goalReached(node, goal):
        return
    nodeList.append(node)
    parentList.append((0,0))
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
node = Node(5,10,0,(0,0))
goal = (15,15)
dijkstra(node,goal)

        

        
        
        
        