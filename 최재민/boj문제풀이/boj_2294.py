import sys

n, k = map(int, input().split())
dp = [100001] * (k+1)
coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

for i in coin:
    if i <= k:
        dp[i] = 1

for i in range(k+1):
    for j in coin:
        if i >= j:
            dp[i] = min(dp[i-j]+1, dp[i])

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])