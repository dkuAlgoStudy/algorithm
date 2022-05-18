import sys

n, m = map(int, input().split())
path = []

for i in range(n):
    path.append(list(map(int, sys.stdin.readline().split())))

dp = [[[100*1000]*3 for _ in range(m)] for _ in range(n+1)]

for i in range(m):
    for j in range(3):
        dp[0][i][j] = 0
for i in range(1, n+1):
    for j in range(m):
        if j == 0:
            dp[i][j][1] = dp[i - 1][j + 1][0] + path[i-1][j];
            dp[i][j][2] = min(dp[i - 1][j][1], dp[i - 1][j + 1][0]) + path[i-1][j];
        elif j == m-1:
            dp[i][j][1] = dp[i - 1][j - 1][2] + path[i-1][j];
            dp[i][j][0] = min(dp[i - 1][j][1], dp[i - 1][j - 1][2]) + path[i-1][j];
        else:
            dp[i][j][0] = min(dp[i - 1][j][1], dp[i-1][j-1][2]) + path[i-1][j]
            dp[i][j][1] = min(dp[i - 1][j + 1][0], dp[i - 1][j - 1][2]) + path[i - 1][j]
            dp[i][j][2] = min(dp[i - 1][j][1], dp[i - 1][j + 1][0]) + path[i - 1][j]

answer = 10000000
for i in range(m):
    if answer > min(dp[n][i]):
        answer = min(dp[n][i])
print(answer)


