from collections import deque

initial_state = [0, 0]  
goal_state = [1, 0]


def possible_moves(state):
    possible_moves = []
    jug1, jug2 = state
    if jug1 < 3:  
        possible_moves.append([3, jug2])
    if jug2 < 5:  
        possible_moves.append([jug1, 5])
    if jug1 > 0:  
        possible_moves.append([0, jug2])
    if jug2 > 0:  
        possible_moves.append([jug1, 0])
    if jug1 > 0 and jug2 < 5:  
        pour = min(jug1, 5 - jug2)
        possible_moves.append([jug1 - pour, jug2 + pour])
    if jug2 > 0 and jug1 < 3:  
        pour = min(jug2, 3 - jug1)
        possible_moves.append([jug1 + pour, jug2 - pour])
    return possible_moves

def bfs():
    visited = [initial_state]
    queue = deque([[initial_state, []]])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            print('No.of States Visited : ', len(visited))
            return path + [state]
        for move in possible_moves(state):
            if move not in visited:
                queue.append([move, path + [state]])
                visited.append(move)
              


def dfs():
    visited = [initial_state]
    stack = [[initial_state, []]]
    while stack:
        state, path = stack.pop()
        if state == goal_state:
            print('No.of States Visited : ', len(visited))
            return path + [state]
        visited.append(state)
        for move in possible_moves(state):
            if move not in visited:
                stack.append([move, path + [state]])
                

def ids():
    for depth in range(20):
        visited = []
        stack = [[initial_state, []]]
        while stack:
            state, path = stack.pop()
            visited.append(state)
            print(depth)
            print(state)
            if state == goal_state:
                print('No.of States Visited : ', len(visited))
                return path + [state]
            if len(path) < depth:
                for move in possible_moves(state):
                    if move not in visited:
                        stack.append([move, path + [state]])
                        

print("BFS:", bfs())
print("DFS:", dfs())
print("IDS:", ids())