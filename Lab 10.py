r=int(input("Enter the number of rules"))
data = []
dict1={}
for i in range(r):
    x = int(input("Enter number of variables"))
    dict = {}
    for j in range (x):
        variable, values=input("Enter the rules").split()
        dict[variable]=values
    data.append(dict)
    action=input("Enter pump action")
    dict1[action]=dict
print(dict1)
print(data)
dup = [x for i, x in enumerate(data) if x in data[:i]]
print(dup)
