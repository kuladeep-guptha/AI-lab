# #bfs with adjacency matrix

# def bfs(graph, start):
#     visited = []
#     queue = [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.append(vertex)
#             queue.extend(graph[vertex])
#     return visited

# def main():
#     n = int(input("Enter number of vertices: "))
#     matrix = []
#     print("Enter adjacency matrix: ")
#     for i in range(n):
#         matrix.append(list(map(int, input().split())))
#     #print(matrix)
#     graph = {}
#     for i in range(n):
#         graph[i] = []
#         for j in range(n):
#             if matrix[i][j] == 1:
#                 graph[i].append(j)
#     print(graph)
#     start = int(input("Enter starting vertex: "))
#     print(bfs(graph, start))
    
# if __name__ == "__main__":
#     main()
    


# # bfs recursion adjacency matrix
# def bfs2(graph, start, visited = None):
#     if visited is None:
#         visited = []
#     visited.append(start)
#     for i in graph[start]:
#         if i not in visited:
#             visited = bfs(graph, i, visited)
#     return visited


# # bfs with adjacency list
# def bfs3(graph, start):
#     visited = []
#     queue = [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.append(vertex)
#             for i in graph[vertex]:
#                 queue.append(i)
#     return visited

# def main():
#     n = int(input("Enter number of vertices: "))
#     graph = {}
#     for i in range(n):
#         graph[i] = list(map(int, input("Enter adjacency list: ").split()))
#     start = int(input("Enter starting vertex: "))
#     print(bfs3(graph, start))
    
# if __name__ == "__main__":
#     main()
    
    

#  #dfs with adjacency list
# def dfs(graph, start):
#     visited = []
#     stack = [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.append(vertex)
#             for i in graph[vertex]:
#                 stack.append(i)
#     return visited


n=4
for i in range(2*n-1):
    for j in range(2*n-1):
        if(j==0 or j==2*n-2):
            print(n,end=" ")
        elif(i==0 or i==2*n-2):
            print(n,end=" ")
        else:
            
            print(k,end=" ")
    print("")
    





