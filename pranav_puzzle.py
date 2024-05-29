from collections import deque

# initial_state = [[2, 8, 3], [1, 6, 4], [7, -1, 5]]
# goal_state = [[1, 2, 3], [8, -1, 4], [7, 6, 5]]

# goal_state = [[2, 8, 3], [1, -1, 4], [7, 6, 5]]

initial_state = [[1, 2, 3], [4, 5, 6], [-1, 7, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]

def is_present(target, visited):
    # for i in range(len(visited)):
    #     for j in range(3):
    #         for k in range(3):
    #             if target[j][k] != visited[i][j][k]:
    #                 return 0
    # return 1
    if target not in visited:
        return 1
    return 0

def possible_moves(state):
    possible_moves = []
    # print(state)
    for i in range(3):
        for j in range(3):
            # print(i, j)
            if state[i][j] == -1:
                row = i
                column = j
                break

    if column+1 <= 2:
        new_state = [row[:] for row in state]
        # print(state)
        temp = new_state[row][column]
        new_state[row][column] = new_state[row][column+1]
        new_state[row][column+1] = temp
        possible_moves.append(new_state)
            
    if row+1 <= 2:
        new_state = [row[:] for row in state]
        # print(new_state)
        temp = new_state[row][column]
        new_state[row][column] = new_state[row+1][column]
        new_state[row+1][column] = temp
        possible_moves.append(new_state)
                
    if row-1 >= 0:
        new_state = [row[:] for row in state]
        # print(state)
        temp = new_state[row][column]
        new_state[row][column] = new_state[row-1][column]
        new_state[row-1][column] = temp
        possible_moves.append(new_state)
                  
    if column-1 >= 0:
        new_state = [row[:] for row in state]
        # print(state)
        temp = new_state[row][column]
        new_state[row][column] = new_state[row][column-1]
        new_state[row][column-1] = temp
        possible_moves.append(new_state)
        
                    
    return possible_moves
                        
            
    
def bfs():
    visited = [initial_state]
    queue = deque([[initial_state, []]])
    
    while queue:
        state, path = queue.popleft()
        # print(visited)
        if state == goal_state:
            print(len(visited))
            return path + [state]
            
        for move in possible_moves(state):
            if not is_present(move, visited):
                queue.append([move, path + [state]])
                visited.append(move)
    
def dfs():
    count = 0
    visited = [initial_state]  
    stack = [[initial_state, []]]
    
    while stack:
        state, path = stack.pop()
        print(state)
        count = count + 1
        # print(visited)
        if state == goal_state:
            print(count)
            return path + [state]
        if is_present(state, visited):
            visited.append(state)
        for move in possible_moves(state):
            # print(move)
            if is_present(move, visited):
                stack.append([move, path + [state]])
    
# print(bfs())   
print(dfs())