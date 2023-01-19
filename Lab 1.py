'''def traverseMatrix(c, row, col, agentr, agentc, path,X):
    if(X==agentr + agentc-2):#flag change
        return('Recharge')
    if(agentr<0 or agentc<0 or agentr >= 5 or agentc >= 5):
        return ""

    if(agentr==row-1 and agentc==col-1):
             print(path+"("+str(row-1)+","+str(col-1)+")")
             return ""
    if(c[agentr][agentc]=='GOLD'):
            print (path+"("+str(agentr)+","+str(agentc)+")")
            return
    traverseMatrix(c,row,col,agentr+1,agentc,path+"("+str(agentr)+","+str(agentc)+")->",X-1)
    traverseMatrix(c,row,col,agentr,agentc+1,path+"("+str(agentr)+","+str(agentc)+")->",X-1)
    traverseMatrix(c,row,col,agentr+1,agentc+1,path+"("+str(agentr)+","+str(agentc)+")->",X-1)

X=21
p=[['O','O','O', 'O', 'O'],['O','GOLD','O','O','O'],['O','O','O', 'O', 'O'],['O','O','O', 'O', 'O'],['O','O','O', 'O', 'O']]
print('The map pre-defined is below :')
for i in p:
    print(i)
print('')
print('Paths are below in coordinate form  : ')
traverseMatrix(p,5,5,0,0,"",X)
#2,3 goldbox
#4,5 entrypoint'''

def agent1 (grid, row, col, current_x, current_y, path):
    if (current_x < 0 or current_y < 0):
        return
    elif (current_x >= row or current_y >= col):
        return
    elif (grid[current_x][current_y] =="X"):
        print (path)
        return
    agent1(grid,row,col,current_x+1,current_y,path+"("+str(current_x)+","+str(current_y)+")")
    agent1(grid, row, col, current_x, current_y+1, path + "(" + str(current_x) + "," + str(current_y) + ")")
    print(current_x, current_y)





p=[['O', 'O', 'O'], ['O', 'O', 'X'], ['O', 'O', 'O']]
for i in p:
    print(i)
print ('')
print("Most optimal paths are:")
agent1(p,3,3,0,0,"")
