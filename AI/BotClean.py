#!/usr/bin/python
# import numpy as np

# Head ends here
def dirty_cells(matrix, val):
    dirty_list = []
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if col == val:
                dirty_list.append([x, y])
    return dirty_list

# def min_dist(b_r, b_c, board):
#     dirty_list = dirty_cells(board, 'd')  # List of position of dirty cells on board
#     dirty_array = np.asarray(dirty_list)
#     dirty_list_size = dirty_array.shape[0]
#     diffMat = np.tile((b_r, b_c), (dirty_list_size, 1)) - dirty_array
#     sqDiffMat = diffMat ** 2
#     sqDistances = sqDiffMat.sum(axis=1)
#     distances = sqDistances ** (0.5)
#     sorted_Indices = distances.argsort()
#     return dirty_list[sorted_Indices[0]]

def min_dist(b_r, b_c, board):
    dirty_list = dirty_cells(board, 'd')  # List of position of dirty cells on board
    return min(dirty_list)

def new_pos(b_r, b_c, d_r, d_c):
    move = None
    row_diff = d_r - b_r
    col_diff = d_c - b_c
    if not row_diff == 0:
        if row_diff > 0:
            move = 'DOWN'
            b_r += 1
        else:
            move = 'UP'
            b_r -= 1
    elif not col_diff == 0:
        if col_diff > 0:
            move = 'RIGHT'
            b_c += 1
        else:
            move = 'LEFT'
            b_c -= 1
    return move, b_r, b_c
    
def next_move(posr, posc, board):
    sum_d = 0
    for i in board:
        sum_d += i.count('d')
    for i in range(sum_d):
        d_r, d_c = min_dist(posr, posc, board)
        total_move = d_r + d_c
        for j in range(total_move):
            move, posr, posc = new_pos(posr, posc, d_r, d_c)
            if move == None:
                break
            print(move)
        print("Clean")
        board[posr][posc] = '-'
    print(board)
    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)