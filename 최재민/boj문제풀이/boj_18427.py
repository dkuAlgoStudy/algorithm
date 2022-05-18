import sys

n, m, h = map(int, input().split())

block = []
dp = [[0]*(h+1) for _ in range(n+1)]
for i in range(n):
    dp[i][0] = 1
for i in range(n):
    block.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    dp[i] = dp[i-1].copy()
    for j in range(1, h+1):
        temp = [0] * (h+1)
        for k in block[i-1]:
            if j-k >= 0:
                dp[i][j] += dp[i-1][j-k]

print(dp[n][h]%10007)