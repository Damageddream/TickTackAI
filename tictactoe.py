"""
Tic Tac Toe Player
"""

import math
import copy

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
    x = 0
    o = 0
    for row in board:
        for mark in row:
            if mark == X:
                x += 1
            elif mark == O:
                o += 1
    if o < x:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for count_row, row in enumerate(board): 
        for count_mark, mark in enumerate(row): 
            if mark == EMPTY:
                actions.add((count_row,count_mark))

    return actions

def result(board, action):
    
    check_player = player(board)
    if not isinstance(action, tuple) or len(action) != 2:
        raise NameError('invalid action')
    for mark in action:
        if not isinstance(mark,int):
           raise NameError('invalid action') 
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = check_player
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def check_rows(board):
        for row in board:
            if all(mark == row[0] for mark in row):
                return row[0]
        return None
    def check_columns(board):
        if(board[0][0] == board[1][0] and board[0][0] == board[2][0]):
            return board[0][0]
        if(board[0][1] == board[1][1] and board[0][1] == board[2][1]):
            return board[0][1]
        if(board[0][2] == board[1][2] and board[0][2] == board[2][2]):
            return board[0][2]
        return None
    def check_diagonal(board):
        if(board[0][0] == board[1][1] and board[0][0] ==board[2][2]):
            return board[0][0]
        if(board[0][2] == board[1][1] and board[0][2]== board[2][0]):
            return board[0][2]
        return None
    rows = check_rows(board)
    columns = check_columns(board)
    diagonal = check_diagonal(board)

    if(rows):
        return rows
    elif(columns):
        return columns
    elif(diagonal):
        return diagonal
    return None
            

def terminal(board):
    
    def filled_board(board):
        for row in board:
            if EMPTY in row:
                return False
        return True
    check_winner = winner(board)
    filled = filled_board(board)
    if(filled or check_winner):
        return True
    return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    check_winner = winner(board)
    if(check_winner == X):
        return 1
    if(check_winner == O):
        return -1
    return 0


def minimax(board):
    
        
    is_terminal = terminal(board)
    if(is_terminal):
        return None

    def find_value(board_state):
        if (terminal(board_state)):
            return utility(board_state)
            
        if(player(board_state) == X):
            v = -2
            for action in actions(board_state):
                v=max(v,find_value(result(board_state,action)))
            return v
        if(player(board_state) == O):
            v = 2
            for action in actions(board_state):
                v=min(v, find_value(result(board_state,action)))
            return v
    
    max_action = [-2]
    min_action = [2]
    best_action = [1]
    
    for action in actions(board):
        if(player(board) == X):
            value = find_value(result(board, action))
            if(max_action[0] < value):
                max_action[0] = value
                best_action[0] = action
        if(player(board) == O):
            value = find_value(result(board, action))
            print(value)
            if(min_action[0] > value):
                min_action[0] = value
                best_action[0] = action      
    return best_action[0]