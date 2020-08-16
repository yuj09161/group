import matplotlib.pyplot as plt,json

with open('export.json','w') as file:
    json.dump(res,file)

for k in range(len(res)):
    x=[]
    y=[]
    for j in range(len(res[k])):
        x.append(res[k][j][0])
        y.append(res[k][j][1])
    plt.scatter(x,y)
plt.show()