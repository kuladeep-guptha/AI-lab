import numpy as np
import random 
import math

cities={'a':[1,1],'b':[2,2],'c':[3,3],'d':[4,4],'e':[5,5],
        'f':[1,2],'g':[1,3],'h':[1,4],'i':[1,5],'j':[1,6],
        'k':[2,6],'l':[3,6],'m':[4,6],'n':[6,6],'o':[5,6]}

def distance(a,b):
    point1=np.array(a)
    point2=np.array(b)
    return np.linalg.norm(point1-point2)


def cost(l):
    cost1=0
    for i in range(len(l)-1):
        a=l[i]
        b=l[i+1]
        cost1=cost1+distance(cities[a],cities[b])
        
        
costs=[]
current=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
#plot the initial path
import matplotlib.pyplot as plt
x=[]
y=[]
for i in current:
    x.append(cities[i][0])
    y.append(cities[i][1])
    
plt.plot(x,y)
plt.show()

costs.append(cost(current))
visited=[]
visited.append(current)
alpha=0.97
T=math.exp(10)
k=0
while(k<1000):
    l=current[:]
    current_value=cost(l)
    i,j=random.sample(current,2)
    l[l.index(i)],l[l.index(j)]=l[l.index(j)],l[l.index(i)]
    visited.append(l)
    next_value=cost(l)
    costs.append(next_value)
    e=next_value-current_value
    if e<0:
        current=l[:]
    else:
        probability=math.exp((-e)/T)
        random_number=random.random()
        if random_number<probability:
            current=l[:]
    T=T*alpha
    k=k+1
    

#plot the cost in each iteration
import matplotlib.pyplot as plt
plt.plot(costs)
plt.show()
print(current)
print(cost(current))




    
        
    
    
    
    
    





