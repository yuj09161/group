import json

color=[]

for a in range(0,256,96):
    for b in range(0,256,96):
        for c in range(0,256,96):
            color.append((a/256,b/256,c/256))

with open('color.json','w') as file:
    json.dump(color,file)