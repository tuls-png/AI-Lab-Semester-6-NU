g = {
'hotel': [('accomodation','is_a')],
'accomodation': [('facility','others')],
'farm': [('accomodation','is_a'),('animal','has')],
'animal': [],
'facility': [],
'pig': [('animal','is_a')],
'sheep': [('animal','is_a')],
'sauna': [('facility','is_a'),('hot', 'is')],
'steambath': [('facility','is_a'),('hot', 'is')],
'hot': [],
'pension': [('accomodation','is_a')],
}
keys = sorted(g.keys())
print(keys)
M = [ [0]*len(keys) for i in range(len(keys)) ]
for vertex_1, row in g.items():
    for vertex_2, weight in row:
        M[keys.index(vertex_1)][keys.index(vertex_2)] = weight
for i in M:
    print(i)

