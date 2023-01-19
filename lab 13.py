import numpy as np
from math import ceil

class Test:
    def __init__(self, ID, LT_Poor, RT_Poor, LT_Av_L, LT_Av_R, UT_Av_L, UT_Av_R, LT_Good, RT_Good):
        self.ID = ID
        self.LT_Poor = LT_Poor
        self.RT_Poor = RT_Poor
        self.LT_Av_L = LT_Av_L
        self.LT_Av_R = LT_Av_R
        self.UT_Av_L = UT_Av_L
        self.UT_Av_R = UT_Av_R
        self.LT_Good = LT_Good
        self.RT_Good = RT_Good


def openLeft(marks, alpha, beta):
    if marks < alpha:
        return 1.0
    if alpha < marks and marks <= beta:
        return (beta - marks)/(beta - alpha)
    else:
        return 0.0


def openRight(marks, alpha, beta):
    if marks < alpha:
        return 0.0
    if alpha < marks and marks <= beta:
        return (marks-alpha)/(beta - alpha)
    else:
        return 1.0


def slopeVal(marks, alpha, beta):
    if alpha < marks <= beta:
        return (marks-alpha)/(beta - alpha)

    return (beta - marks)/(beta - alpha)


def triangular(marks, a, b, c):
    return max(min((marks-a)/(b-a), (c-marks)/(c-b)), 0)


def partition(test: Test, marks):
    poor = openLeft(marks, test.LT_Poor, test.RT_Poor)
    good = openRight(marks, test.LT_Good, test.RT_Good)

    if marks < test.LT_Av_L:
        average = 0.0
    if marks >= test.LT_Av_L and marks <= test.LT_Av_R:
        average = slopeVal(marks, test.LT_Av_L, test.LT_Av_R)
    if marks > test.LT_Av_R and marks <= test.UT_Av_L:
        average = 1.0
    if marks > test.UT_Av_L and marks <= test.UT_Av_R:
        average = slopeVal(marks, test.UT_Av_L, test.UT_Av_R)
    if marks > test.UT_Av_R:
        average = 0.0

    return poor, average, good





def centerOfGravity(tests, choice):
    domain = np.arange(0, 100, 0.1)

    def function1(x):
        poor1, average1, good1 = partition(tests[0], x)
        poor2, average2, good2 = partition(tests[1], x)
        poor3, average3, good3 = partition(tests[2], x)

        R1 = max(max(poor1, poor2, poor3), max(average1, average2, average3))
        R2 = min(max(average1, average2, average3), max(good1, good2, good3))

        if choice == 1:
            return R1

        return R2

    def function2(x):
        return function1(x)*x


    num = 0
    denom = 0
    for x in domain:
        num += function2(x)
        denom += function1(x)

    return num/denom

    
    # Simpsons formula
    N = ceil((b-a+1)/0.01)
    Dx = (b-a)/N
    coeff = function2(0)
    num = 0
    denom = 1
    
    # Numerator
    for i in range(1,N):
        if i%2 == 0:
            coeff += 2*function2(i)
        else:
            coeff += 4*function2(i)
    
    coeff += function2(N)
    num = (Dx/3)*coeff
    
    # Denominator
    coeff = function1(0)
    for i in range(1,N):
        if i%2 == 0:
            coeff += 2*function1(i)
        else:
            coeff += 4*function1(i)
    coeff += function1(N)
    
    denom = (Dx/3)*coeff
    return num/denom
    

LT_Poor, UT_Poor, LT_Av_L, LT_Av_R, UT_Av_L, UT_Av_R, LT_Good, UT_Good = 0, 0, 0, 0, 0, 0, 0, 0
inputs = [[28, 60, 25, 36, 60, 80, 31, 80], [22, 62, 26,
                                             34, 60, 74, 30, 78], [21, 58, 25, 35, 55, 75, 33, 85]]

tests = []
for j in range(0, 3):
    # LT_Poor, RT_Poor, LT_Av_L, LT_Av_R, UT_Av_L, UT_Av_R, LT_Good, RT_Good = list(map(int, input().split()))
    LT_Poor, RT_Poor, LT_Av_L, LT_Av_R, UT_Av_L, UT_Av_R, LT_Good, RT_Good = inputs[j]
    tests.append(Test(j + 1, LT_Poor, RT_Poor, LT_Av_L, LT_Av_R,
                 UT_Av_L, UT_Av_R, LT_Good, RT_Good))




# Choice 1 for membership Poor OR Average, else Average AND Good
choice = 1
membership = "(Poor OR Average)" if choice == 1 else "(Average AND Good)"
print( membership, centerOfGravity(tests, choice))
choice = 0
membership = "(Poor OR Average)" if choice == 1 else "(Average AND Good)"
print(membership, centerOfGravity(tests, choice))
