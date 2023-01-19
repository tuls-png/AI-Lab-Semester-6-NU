import random

def function(x):
    return (64 - x**2)**2

def fitnessfunction (x):
    fit = function(x)
    if fit == 0:
        return 10000
    else:
        return (1/fit)

randomsolution =[]
for s in range (100):
    randomsolution.append((random.randint(0, 15)))
print("Random Solution", randomsolution)

for i in range(1, 6):
    list1 = []
    for s in randomsolution:
        print()
        print()
        list1.append((fitnessfunction(s), s))
        list1.sort()
        list1.reverse()
        print("For Generation", i)
        print()
        print("Best Solution is", list1[0])

        if(list1[0][0]>999):
            break
        list2 = []
        for s in list1:
            list2.append(s[1])

        children = []
        for j in range(100):
            new_ele = random.choice(list2) * 0.1
            children.append(new_ele)
        solution = children