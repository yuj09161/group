import random,group,matplotlib.pyplot as plt

GROUPS=10 #must be >=2
data=[]
for k in range(100):
    data.append((int(random.random()*100000),int(random.random()*100000)))
res=group.main(data,GROUPS)
for k in range(len(res)):
    x=[]
    y=[]
    for j in range(len(res[k])):
        x.append(res[k][j][0])
        y.append(res[k][j][1])
    plt.scatter(x,y)
plt.show()