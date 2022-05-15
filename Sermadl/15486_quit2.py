import sys

N = int(input())
dp = [0] * (N + 1)
t, p = [], []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

m = 0
for i in range(N):
    m = max(m, dp[i])
    if i + t[i] > N:
        continue
    dp[i + t[i]] = max(m + p[i], dp[i + t[i]])

print(max(dp))
