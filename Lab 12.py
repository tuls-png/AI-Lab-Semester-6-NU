LTPoor, RTPoor = 37.5, 62.5
LTAvL, LTAvR, UTAvL, UTAvR = 25, 40, 62.5, 80
LTGood, RTGood = 37.5, 80

marks = list(map(float, input().split()))

#For Poor
poor=[0,0,0]
for i in range(len(marks)):
    if 0<marks[i]<=LTPoor:
        poor[i]=1
    elif LTPoor<marks[i]<=RTPoor:
        poor[i]=marks[i]*(-1/25)+2.5
    elif RTPoor<marks[i]:
        poor[i]=0


#For Average
average=[0,0,0]
for i in range(len(marks)):
    if LTAvL<marks[i]<=LTAvR:
        average[i]=marks[i]*(1/15)-1.66
    elif LTAvR<marks[i]<=UTAvL:
        average[i]=1
    elif UTAvL<marks[i]<=UTAvR:
        average[i]=marks[i]*(-1/17.5)+4.57

#For Good
good=[0,0,0]
for i in range(len(marks)):
    if 0<marks[i]<=LTGood:
        good[i]=0
    elif LTGood<marks[i]<RTGood:
        good[i]=marks[i]*(1/42.5)-0.88
    elif RTGood<marks[i]:
        good[i]=1

result=[0,0,0]
for i in range(3):
    if good[i]>poor[i] and good[i]>average[i]:
        marks[i]="Good"
        result[i]=max(poor[i], average[i], good[i])
    elif poor[i]>good[i] and poor[i]>average[i]:
        marks[i]="Poor"
        result[i] = max(poor[i], average[i], good[i])
    elif average[i]>poor[i] and average[i]>good[i]:
        marks[i]="Average"
        result[i] = max(poor[i], average[i], good[i])

print(marks)
print('Poor', poor)
print('Average', average)
print('Good', good)
print(result)

strength=[0,0,0,0]
if marks[0]=="Poor" or "Average" and marks[1]=="Poor" or "Average" and marks[2]=="Poor" or "Average":
    strength[0]=max(result)
elif marks[0]=="Poor" or "Average" and marks[1]=="Poor" or "Average" and marks[2]=="Good":
    strength[1] = max(result)
elif marks[0]=="Poor" or "Average" and marks[1]=="Good" and marks[2]=="Good":
    strength[2] = max(result)
elif marks[0] and marks[1] and marks[2] == "Good":
    strength[3] = max(result)
print(strength)









