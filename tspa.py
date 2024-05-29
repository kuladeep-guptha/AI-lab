L=list()
l=list()

# m=int(input("enter the no.of cities"))
# for i in range(m):
#     for j in range(m):
#         l.append(0)
#     L.append(l)
#     l=[]

# print(L)

# for i in range(m):
#     for j in range(i,m):
#         if(i==j):
#             INF=float('inf')
#             L[i][j]=INF
#         else:
#             print("enter the distance between",i,"and",j)
#             k=int(input())
#             L[i][j]=k
#             L[j][i]=k
# # for i in range(m):
# #     L[i].insert(0,0)
# print(L)
INF=float('inf')
L=[[INF,12,10,19,8],
   [12,INF,3,7,6],
   [10,3,INF,2,20],
   [19,7,2,INF,4],
   [8,6,20,4,INF]]
m=5

def krushkals(L,k):
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    def union(i, j):
        a = find(i)
        b = find(j)
        parent[a] = b
 
# Finds MST using Kruskal's algorithm 
    def kruskalMST(cost,k):
        mincost = 0 # Cost of min MST
    
        # Initialize sets of disjoint sets
        for i in range(k):
            parent[i] = i
    
        # Include minimum weight edges one by one 
        edge_count = 0
        while edge_count < k- 1:
            min = INF
            a = -1
            b = -1
            for i in range(k):
                for j in range(k):
                    if find(i) != find(j) and cost[i][j] < min:
                        min = cost[i][j]
                        a = i
                        b = j
            union(a, b)
            # print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
            edge_count += 1
            mincost += min
    
        return mincost
    return(kruskalMST(L,k))
    
    
    
parent = [i for i in range(m)]    
def heuristics(path):
    h=[0]*m
    new=[x.copy() for x in L]
    print("new1",new)
    # for i in path:
    #     print("i=",i)
    #     # INF=float('inf')
    #     # new[i]=[INF]*m #  
    #     new.pop(i)
    #     for row in new:
    #         row.pop(i)
    #     # new = [[row[k] if k != i else INF for k in range(len(row))] for row in new]
    #     print("new",new)
    
    new = [[INF if i in path[1:-1] or j in path[1:-1] else L[i][j] for i in range(m)] for j in range(m)]
    print("new2",new)
    
    h=krushkals(new,m-len(path))
    
    return h


# H=heuristics()
# print(H)


def tspa(L):
    start=0
    INF=float('inf')
    min_cost=INF
    min_path=[]
    queue=[([start],0,0)]
    while queue:
        path,cost,fn=queue.pop(0)
        node=path[-1]
        for i in range(m):
            if L[node][i]!=INF and i not in path:
                newpath=path+[i]
                if len(newpath)==m:
                    cost=cost+L[node][i]+L[i][start]
                    min_cost=cost
                    min_path=newpath
                    return newpath,min_cost
                newcost=cost+L[node][i]
                h1=heuristics(path)
                newfn=newcost+h1
                queue.append((newpath,newcost,newfn))
                queue.sort(key=lambda x:x[2])
    
    return min_path,min_cost
                
        
print(tspa(L))     
            
    






        