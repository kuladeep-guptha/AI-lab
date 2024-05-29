#solve the tic-tac-toe probelm starting from an empty state . trace the alpha-beta pruning method to find the best path to the goal


initial_state=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
player = 'X'
opponent = 'O'
def print_board(board):
    for i in range(3):
        for j in range(3):
            if j!=2:
                print(board[i][j],end=" | ")
            else:
                print(board[i][j])
        if i!=2:
            print("---------")
    print()
    
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                return True
    return False

def evaluate(board):
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][0]==player:
                return 10
            elif board[i][0]==opponent:
                return -10
    for i in range(3):
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            if board[0][i]==player:
                return 10
            elif board[0][i]==opponent:
                return -10
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]==player:
            return 10
        elif board[0][0]==opponent:
            return -10
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]==player:
            return 10
        elif board[0][2]==opponent:
            return -10
    return 0

def minimax(board,depth,isMax):
    score = evaluate(board)
    if score==10:
        return score
    if score==-10:
        return score
    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]=player
                    best = max(best,minimax(board,depth+1,not isMax))
                    board[i][j]=' '
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]=opponent
                    best = min(best,minimax(board,depth+1,not isMax))
                    board[i][j]=' '
        return best
    
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]=player
                moveVal = minimax(board,0,False)
                board[i][j]=' '
                if moveVal>bestVal:
                    bestMove = (i,j)
                    bestVal = moveVal
    return bestMove




