import sys

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        row = i + board[i][j]
        col = j + board[i][j]

        if row < n:
            dp[row][j] += dp[i][j]
        if col < n:
            dp[i][col] += dp[i][j]

print(dp[n-1][n-1])
