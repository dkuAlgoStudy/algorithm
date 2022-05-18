def pop(m,n,board):
    pop = set()
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == board[i-1][j] == board[i][j-1] != 'x':
                pop |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
    for i, j in pop:
        board[i][j] = 0
    for i in range(len(board)):
        line = ['x'] * board[i].count(0)
        board[i] = line + [block for block in board[i] if block != 0]
    print(pop)
    return len(pop)


def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    while True:
        temp = pop(m, n, board)
        if temp == 0:
            return answer
        answer += temp