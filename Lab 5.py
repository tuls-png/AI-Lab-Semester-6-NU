def travel(a, n, d, unvisited, visited):
    for i in range(n):
        if not unvisited[i]:
            visited.append(a[i])
            unvisited[i] = True
            if len(visited) == N:
                print(visited)
            travel(a, n, d, unvisited, visited)
            visited.pop()
            unvisited[i] = False
    return

N = int(input("Enter the number of jobs : "))
print("The state space tree is : ")
a = [j for j in range(1, N+1)]
n = len(a)
unvisited = [False] * len(a)
travel(a, n, n, unvisited, [])




class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# create root
root = Node(1)
''' following is the tree after above statement
        1
      /   \
     None  None'''

root.left = Node(2);
root.right = Node(3);

''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
   None None None None'''

root.left.left = Node(4);
print(root.val)