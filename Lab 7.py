'''import math
def minimax(cd, node, maxTurn, leafnodes, td):
    if (cd == td):
        return leafnodes[node]
    if (maxTurn):
        return max(minimax(cd + 1, node * 2, False, leafnodes, td),
                   minimax(cd + 1, node * 2 + 1, False, leafnodes, td))

    else:
        return min(minimax(cd + 1, node * 2, True, leafnodes, td),
                   minimax(cd + 1, node * 2 + 1, True, leafnodes, td))



leafnodes = [int(item) for item in input("Enter the list items : ").split()]
depth = math.log(len(leafnodes), 2)
print("Root node")
print(minimax(0, 0, True, leafnodes, depth))'''



import math
MAX, MIN = 99999, -99999
def minimax(cd, nodeIndex, maximizingPlayer, values, alpha, beta, td):
    if cd == td:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = minimax(cd + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta, td)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(cd + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta, td)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = [int(item) for item in input("Enter the list items : ").split()]
d = math.log(len(values), 2)
print("Root node", minimax(0, 0, True, values, MIN, MAX, d))