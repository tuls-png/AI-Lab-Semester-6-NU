def travel(a, n, d, unvisited, visited, path):
    for i in range(n):
        if not unvisited[i]:
            visited.append(a[i])
            unvisited[i] = True
            print(unvisited)
            print(visited)
            travel(a, n, d, unvisited, visited, path)

            visited.pop()
            print("--")
            print(visited)
            print("--")
            unvisited[i] = False
            print(unvisited)

    return


x = int(input("enter"))
a = [j for j in range(1, x)]
n = len(a)
unvisited = [False] * len(a)
path = []
travel(a, n, n, unvisited, [], path)
print(path)
