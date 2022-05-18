import sys

n = int(input())
consult = []
dp = [0] * (n+1)

for _ in range(n):
    consult.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    if consult[i][0] <= n-i:
        dp[i+consult[i][0]] = max(dp[i+consult[i][0]],dp[i]+consult[i][1])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])


