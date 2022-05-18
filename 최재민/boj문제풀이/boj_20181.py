import sys
n, k = map(int, sys.stdin.readline().split())
temp, ans, sum_a = 0, 0, 0
arr = list(map(int, sys.stdin.readline().split()))
l, r = 0, 0
dp = [0] * (n+1)

while True:
    if sum_a >= k:
        if l == 0:
            temp = 0
        else:
            temp = max(temp, dp[l - 1])
        dp[r-1] = max(dp[r-1], temp + sum_a - k)
        sum_a -= arr[l]
        l += 1
    elif r == n:
        break
    else:
        sum_a += arr[r]
        r += 1
for i in range(n):
    ans = max(ans, dp[i])

print(ans)
