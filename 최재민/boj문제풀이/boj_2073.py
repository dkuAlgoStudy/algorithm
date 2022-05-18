import sys

d, p = map(int, input().split())

dp = [0] * (d+1)
pipe = []

for _ in range(p):
    pipe.append(list(map(int, sys.stdin.readline().split())))
dp[0] = 100001
pipe.sort()

for i in range(p):
    for j in range(d, pipe[i][0]-1, -1):
        dp[j] = max(dp[j], min(pipe[i][1], dp[j-pipe[i][0]]))

print(dp[d])
