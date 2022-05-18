import sys

n = int(input())

idle = []

for _ in range(n):
    idle.append(int(input()))

dp = [0] * n
for i in range(n):
    for j in range(i):
        if idle[i] > idle[j]:
            if dp[i] < dp[j]:
                dp[i] = dp[j]
    dp[i] += 1

print(n-max(dp))