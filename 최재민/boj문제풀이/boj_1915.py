import sys

n, m = map(int, input().split())

square = []
dp = [[0]*(m+1) for _ in range(n+1)]

for _ in range(n):
    square.append(list(map(int,sys.stdin.readline().rstrip())))

ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if square[i-1][j-1] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j],dp[i-1][j-1]) + 1
            if dp[i][j] > ans:
                ans = dp[i][j]

print(ans**2)