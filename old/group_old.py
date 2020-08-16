import json,random as rand,copy
import matplotlib.pyplot as plt, numpy as np


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


def graph(group,avg,n,turn,priv_avg):
    print(turn,avg,priv_avg)
    for k in range(n):
        x=[]
        y=[]
        for j in range(len(group[k])):
            x.append(group[k][j][0])
            y.append(group[k][j][1])
        plt.scatter(x,y,color=COLORS[k],marker=k)
        plt.scatter(*avg[k],color=COLORS[k],marker='*')
        plt.scatter(*priv_avg[k],color=COLORS[k])
    for k in range(len(priv_avg)):
        plt.scatter(*priv_avg[k],color=COLORS[k])
    plt.show()


def main(data,n):
    avg=[]
    priv_avg=[]
    l=len(data)
    ld=len(data[0])
    for k in rand.sample(range(l),n):
        avg.append(data[k])
        priv_avg.append(None)
    print(avg)
    turn=0
    while True:
        #make groups
        group=[]
        for k in range(n):
            group.append([])
        #find closest group
        for d in data:
            #m=0
            dst=[]
            for j in range(n):
                dst.append(dist(d,avg[j]))
                #if dist(d,avg[j])>dist(d,avg[j+1]):
                    #m=j+1
            print(dst,dst.index(min(dst)))
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
        #graph(group,avg,n,turn,priv_avg)
        #if end
        if avg==priv_avg or turn>100:
            return group
        else:
            turn+=1


if __name__=='__main__':
    GROUPS=10 #must be >=2
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
    plt.show()