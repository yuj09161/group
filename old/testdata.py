import json,random

data=[]
for k in range(100):
    data.append((int(random.random()*100000),int(random.random()*100000)))

with open('testdata.json','w',encoding='utf-8') as file:
    json.dump(data,file)