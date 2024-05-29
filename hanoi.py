# class Tower:
#     def __init__(self,ndisks,ntowers):
#         self.num_of_disks=ndisks
#         self.ntowers=ntowers
#         self.towers=[[] for _ in range(ntowers)]
#         self.towers[0]=[i for i in range(ndisks,0,-1)]
#         self.final_state=[[] for _ in range(ntowers)]
#         self.final_state[-1]=[i for i in range(ndisks,0,-1)]
#         print(self.towers)
#     def display(self):
#         print(self.towers)
#     def valid_move(self,fromt,tot):
#         if not self.towers[fromt]:
#             return False
#         if not self.towers[tot] or self.towers[fromt][-1]<self.towers[tot][-1]:
#             return True
#         return False
#     def make_move(self,fromt,tot):
#         k=self.towers[fromt].pop(-1)
#         self.towers[tot].append(k)
#     def is_goal(self):
#         return self.towers==self.final_state
#     def BFS(self):
#         queue=[self.towers]
#         visited=list()
#         while queue:
#             current_state=queue.pop(0)
#             self.towers=current_state
#             new=[x.copy() for x in current_state]
#             print("new=",new)
#             if new not in visited :
#                 visited.append(new)
#             for i in range(self.ntowers):
#                 for j in range(self.ntowers):
                   
#                     if i!=j and self.valid_move(i,j):
#                         # print(new)
#                         print(i,j)
#                         print("towers=",self.towers)
#                         self.make_move(i,j)
#                         # self.display()
#                         if self.is_goal():
#                             return visited
#                         if self.towers not in queue:
#                             print("t=",self.towers)
#                             queue.append([x.copy() for x in self.towers])
#                         self.towers=new
#                     # print("towers2=",self.towers)
                        
#         return False
    
                        
                        

# t=Tower(3,3)
# x=t.BFS()
# print("x=",x[0],x[1],x[2],x[4])
# for i in x:
#     print(i)



class Tower:
    def __init__(self,ndisks,ntowers):
        self.num_of_disks=ndisks
        self.ntowers=ntowers
        self.towers=[[] for _ in range(ntowers)]
        self.towers[0]=[i for i in range(ndisks,0,-1)]
        self.final_state=[[] for _ in range(ntowers)]
        self.final_state[-1]=[i for i in range(ndisks,0,-1)]
        print(self.towers)
    def valid_move(self,fromt,tot):
        if not self.towers[fromt]:
            return False
        if not self.towers[tot] or self.towers[fromt][-1]<self.towers[tot][-1]:
            return True
        return False
    def is_goal(self):
        return self.towers==self.final_state
    def BFS(self):
        queue=[self.towers]
        visited=list()
        while queue:
            current_state=queue.pop(0)
            self.towers=current_state
            print("towers1=",self.towers)
            # print("new=",new)
            if current_state not in visited :
                visited.append(current_state)
            for i in range(self.ntowers):
                for j in range(self.ntowers):
                    print(i,j)
                    new=[x.copy() for x in current_state]
                    if i!=j and self.valid_move(i,j):
                        
                        print("towers=",self.towers)
                        # self.make_move(i,j)
                        k=new[i].pop(-1)
                        new[j].append(k)
                        # self.display()
                        print("new=",new)
                        if self.is_goal():
                            return visited
                        if new not in visited:
                            print("t=",new)
                            queue.append([x.copy() for x in new])
                        # self.towers=new
        return False
    
    def DFS(self):
        self.towers=[[i for i in range(3,0,-1)],[],[]]
        stack=[self.towers]
        visited=list()
        while stack:
            current_state=stack.pop(-1)
            self.towers=current_state
            print("towers1=",self.towers)
            # print("new=",new)
            if current_state not in visited :
                visited.append(current_state)
            for i in range(self.ntowers):
                for j in range(self.ntowers):
                    print(i,j)
                    new=[x.copy() for x in current_state]
                    if i!=j and self.valid_move(i,j):
                        
                        print("towers=",self.towers)
                        # self.make_move(i,j)
                        k=new[i].pop(-1)
                        new[j].append(k)
                        # self.display()
                        print("new=",new)
                        if self.is_goal():
                            return visited
                        if new not in visited:
                            print("t=",new)
                            stack.append([x.copy() for x in new])
                        # self.towers=new
        return False
    
    
    def DLS(self,stack,depth):
        print(depth)
        visited=list()
        while stack:
            current_state=stack.pop(-1)
            self.towers=current_state[0]
            # print("towers1=",self.towers)
            # print("new=",new)
            if current_state[0] not in visited :
                print(current_state[0])
                visited.append(current_state[0])
            
            if current_state[1]<depth:
                for i in range(self.ntowers):
                    for j in range(self.ntowers):
                        # print(i,j)
                        new=[x.copy() for x in current_state[0]]
                        if i!=j and self.valid_move(i,j):
                            
                            # print("towers=",self.towers)
                            # self.make_move(i,j)
                            k=new[i].pop(-1)
                            new[j].append(k)
                            # self.display()
                            # print("new=",new)
                            if self.is_goal():
                                return visited
                            # print("visited=",visited)
                            if new not in visited :
                                # print("t=",new)
                                stack.append([[x.copy() for x in new],current_state[1]+1])
                            # self.towers=new
        return False
    
    
    
    def IDS(self):
        depth=0
        while True:
            self.towers=[[i for i in range(3,0,-1)],[],[]]
            stack=[[self.towers,0]]
            result=self.DLS(stack,depth)
            if result:
                return result
            depth+=1
    
                        
                        
                
                
        
        


t=Tower(3,3)
# x=t.BFS()
# # print("x=",x[0],x[1],x[2],x[4])
# print(x)
# print(len(x))
# is_unique = all(len(subsublist) == len(set(subsublist)) for sublist in x for subsublist in sublist)
# print(is_unique)

# y=t.DFS()
# print(y)
# print(len(y))
# is_unique = all(len(subsublist) == len(set(subsublist)) for sublist in y for subsublist in sublist)
# print(is_unique)

z=t.IDS()
print(z)
print(len(z))
# is_unique = all(len(subsublist) == len(set(subsublist)) for sublist in z for subsublist in sublist)
# print(is_unique)





