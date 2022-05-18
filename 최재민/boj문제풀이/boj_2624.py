import sys

t = int(input())
k = int(input())
dp = [[0] * 10001 for i in range(k+1)]
for i in range(k+1):
    dp[i][0] = 1
coin = [[0, 0]]
for i in range(k):
    value, num = map(int, sys.stdin.readline().split())
    coin.append([value, num])
coin.sort()
for i in range(1, k+1):
    for j in range(coin[i][1]+1):
        for p in range(t+1):
            if p+j*coin[i][0] == 0:
                continue
            if p+j*coin[i][0] < t+1:
                dp[i][p+j*coin[i][0]] += dp[i-1][p]
            else:
                break

print(dp[k][t])
