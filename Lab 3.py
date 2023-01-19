import random
def travel(a, n, d, unvisited, visited, path):
    for i in range(n):
        if not unvisited[i]:
            visited.append(a[i])
            unvisited[i] = True
            travel(a, n, d, unvisited, visited, path)
            visited.pop()
            unvisited[i] = False
            if not visited:
                break
    l = []
    if len(visited) == x - 1:
        for i in range(len(visited)):
            l.append(visited[i])
        l.append(1)

        routes.append(l)
        cost=[]
        for i in range(len(l)-1):
            cost.append(matrix[l[i]-1][l[i+1]-1])
        allcosts.append(sum(cost))
        print(l)


    return
x=int(input("enter"))
a = [j for j in range(1, x)]
print(a)
n = len(a)
unvisited = [False] * len(a)
path = []
routes=[]
allcosts=[]

matrix=[[random.randint(1, 10) for j in range(1, x)] for i in range(1, x)]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            matrix[i][j] = 0
print("Weight Matrix - ", matrix)
travel(a, n, n, unvisited, [], path)
print(allcosts)

