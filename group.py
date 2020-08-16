import json,copy
import random as rand


with open('color.json','r') as file:
    COLORS=json.load(file)


def dist(v1,v2):
    l=len(v1)
    assert l==len(v2)
    length=0
    for k in range(l):
        length+=abs(v1[k]-v2[k])**2
    return length**.5


def get_avg(data):
    l=len(data)
    ld=len(data[0])
    avg=[0]*ld
    for k in range(l):
        assert len(data[k])==ld
        for j in range(ld):
            avg[j]+=data[k][j]
    for k in range(ld):
        avg[k]/=l
    return avg


def main(data,n):
    assert data, 'No data'
    assert n>1, 'Group size must bigger than 1'
    avg=[]
    priv_avg=[]
    l=len(data)
    ld=len(data[0])
    for k in rand.sample(range(l),n):
        avg.append(data[k])
        priv_avg.append(None)
    turn=0
    while True:
        #make groups
        group=[]
        for k in range(n):
            group.append([])
        #find closest group
        for d in data:
            dst=[]
            for j in range(n):
                dst.append(dist(d,avg[j]))
            m=dst.index(min(dst))
            group[m].append(d)
        #copy previous value
        priv_avg=copy.deepcopy(avg)
        t=n
        #exclude blank group
        n=0
        t_g=[]
        for k in range(t):
            if group[k]:
                n+=1
                t_g.append(group[k])
        group=t_g
        #get current group average
        for k in range(n):
            avg[k]=get_avg(group[k])
        #if end
        if avg==priv_avg or turn>100:
            return group
        else:
            turn+=1
            print(f'pass: {turn}')


if __name__=='__main__':
    import matplotlib.pyplot as plt, numpy as np
    GROUPS=10
    data=[]
    for k in range(100):
        data.append((int(rand.random()*100000),int(rand.random()*100000)))
    res=main(data,GROUPS)
    for k in range(len(res)):
        x=[]
        y=[]
        for j in range(len(res[k])):
            x.append(res[k][j][0])
            y.append(res[k][j][1])
        plt.scatter(x,y)
    plt.show(figsize=(20,20),dpi=80)
    with open('export.json','w') as file:
        json.dump(res,file)