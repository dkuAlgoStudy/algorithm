import sys
c, n = map(int, input().split())

dp = [int(1e9)] * (c+101)
dp[0] = 0
coin = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for cost, people in coin:
    for now in range(people, c+101):
        dp[now] = min(dp[now], dp[now-people]+cost)
print(min(dp[c:-1]))
