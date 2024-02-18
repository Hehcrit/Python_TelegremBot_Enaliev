board = {1: ['1', '2', '3'],
         2: ['4', '5', '6'],
         3: ['7', '8', '9']
         }

def draw_board(board):
    for i in range(3):
        print(" | ".join(board[i+1]))
        print("---------")

draw_board(board)