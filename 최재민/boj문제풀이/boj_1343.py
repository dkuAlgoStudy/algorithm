board = input()
i = 0


while i < len(board):
    if board[i:i+4] == 'XXXX':
        board = board.replace('X', 'A', 4)
        i = i+4
    elif board[i:i+2] == 'XX':
        board = board.replace('X', 'B', 2)
        i = i+2
    elif board[i] == '.':
        i = i+1
    else:
        board = -1
        break

print(board)
