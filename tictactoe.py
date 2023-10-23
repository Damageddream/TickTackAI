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
        raise NameError('valid action')
    for mark in action:
        if not isinstance(mark,int):
           raise NameError('valid action') 
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
    def max_value(board_max):
        if(terminal(board_max)):
            return utility(board_max)
        v = -2
        for action in actions(board_max):
            v = max(v, min_value(result(board_max, action)))
        return v
    def min_value(board_min):
        if(terminal(board_min)):
            return utility(board_min)
        v = 2
        for action in actions(board_min):
            v = min(v, max_value(result(board_min, action)))
        return v

    all_actions = actions(board)
    player_turn = player(board)

    best_action_max = -2
    best_action_min = 2
    return_action = [1]


    for action in all_actions:
        if(player_turn == X):
            if(max_value(board) > best_action_max):
                return_action[0] = action
        if(player_turn == O):
            if(min_value(board) < best_action_min):
                return_action[0] = action
                
    return action
                

        
            

    
        