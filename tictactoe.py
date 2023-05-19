"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count=sum([row.count(X) for row in board])
    o_count=sum([row.count(O) for row in board])
    if x_count==o_count:
        return X
    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                action.add((i,j))
    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board=initial_state()
    row,col=action
    recommended_actions=actions(board)
    if action in recommended_actions:
        for i in range(3):
            for j in range(3):
                new_board[i][j]=board[i][j]
        new_board[row][col]=player(board)
        return new_board
    raise Exception("The action is not a valid action for the board")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking diagonals
    
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=EMPTY:
        return board[0][0]
    if board[2][0]==board[1][1]==board[0][2] and board[2][0]!=EMPTY:
        return board[2][0]
    
    # checking columns
    
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=EMPTY:
            return board[0][i]
        
    # checking rows
    
    for row in board:
        if row[0]==row[1]==row[2] and row[0]!=EMPTY:
            return row[0]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=EMPTY:
        return True
    if board[2][0]==board[1][1]==board[0][2] and board[2][0]!=EMPTY:
        return True
    
    # checking columns
    
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=EMPTY:
            return True
        
    # checking rows
    
    for row in board:
        if row[0]==row[1]==row[2] and row[0]!=EMPTY:
            return True
        
    # checking if game is still going on
    
    for row in board:
        if EMPTY in row:
            return False
        
    # Draw
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=EMPTY:
        if board[0][0]==X:
            return 1
        else: return -1
    if board[2][0]==board[1][1]==board[0][2] and board[2][0]!=EMPTY:
        if board[2][0]==X:
            return 1
        else: return -1
    
    # checking columns
    
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=EMPTY:
            if board[0][i]==X:
                return 1
            else: return -1
        
    # checking rows
    
    for row in board:
        if row[0]==row[1]==row[2] and row[0]!=EMPTY:
            if row[0]==X:
                return 1
            else: return -1
        
    # Draw
    return 0

def help_minimax(board):
    if terminal(board):
        return None,utility(board)
    
    current_player=player(board)
    
    if current_player==X:
        best_utility=float("-inf")
        move=None    
        for action in actions(board):
            new_board=result(board, action)
            _,minimax_result=help_minimax(new_board)
            if minimax_result>best_utility:
                best_utility=minimax_result
                move=action
        return move,best_utility
    
    if current_player==O:
        best_utility=float("inf")
        move=None
        for action in actions(board):
            new_board=result(board, action)
            _,minimax_result=help_minimax(new_board)
            if minimax_result<best_utility:
                best_utility=minimax_result
                move=action
        return move,best_utility

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_move,super_utility=help_minimax(board)
    return best_move







