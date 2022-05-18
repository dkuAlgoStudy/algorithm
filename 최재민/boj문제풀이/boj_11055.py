n = int(input())
a = list(map(int, input().split()))

dp = [0 for i in range(n+1)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            if dp[i] < dp[j]:
                dp[i] = dp[j]
    dp[i] += a[i]
print(max(dp))

