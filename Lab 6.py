'''class Node:
    def __init__(self, val):
        self.left=None
        self.right=None
        self.val=val
def tree(coin,root):
    if coin<=0:
        return
    root.left=Node(coin-1)
    root.right=Node(coin-2)

coin=int(input("enter"))
root=Node(coin)
tree(coin, root)'''
from collections import deque
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def tree(x, root):
    if x <= 0:


        return
    root.left = Node(x-2)
    root.right = Node(x-1)
    tree(x-2, root.left)

    tree(x-1, root.right)
def isLeaf(node):
    return node.left is None and node.right is None

# Recursive function to find paths from the root node to every leaf node
def printRootToLeafPaths(node, path):
    # base case
    if node is None:
        return

    # include the current node to the path
    path.append(node.data)

    # if a leaf node is found, print the path
    if isLeaf(node):
        print(list(path))

    # recur for the left and right subtree
    printRootToLeafPaths(node.left, path)
    printRootToLeafPaths(node.right, path)

    # backtrack: remove the current node after the left, and right subtree are done
    path.pop()

# The main function to print paths from the root node to every leaf node
def printRootToLeafPath(root):
    # list to store root-to-leaf path
    path = deque()
    printRootToLeafPaths(root, path)



x = int(input("Enter value of coins: "))
root = Node(x)
tree(x, root)
printRootToLeafPath(root)
p1=[]
p2=[]