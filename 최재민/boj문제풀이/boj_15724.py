import sys
n, m = map(int, input().split())
arr = []
dp = [[0]*(m+1) for i in range(n+1)]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]-dp[i][j] + arr[i][j]

k = int(input())
for _ in range(k):
    s_x, s_y, e_x, e_y = map(int, sys.stdin.readline().split())
    print(dp[e_x][e_y]-(dp[s_x-1][e_y] + dp[e_x][s_y-1] - dp[s_x-1][s_y-1]))


