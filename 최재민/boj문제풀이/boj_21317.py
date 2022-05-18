n = int(input())

s_jump = []
l_jump = []
dp = [0] * (n)

for _ in range(n-1):
    small, large = map(int, input().split())
    s_jump.append(small)
    l_jump.append(large)
k = int(input())
if n>= 2:
    dp[1] = s_jump[0]
if n>= 3:
    dp[2] = min(s_jump[0]+s_jump[1], l_jump[0])
for i in range(3, n):
    dp[i] = min(dp[i-1]+s_jump[i-1], dp[i-2]+l_jump[i-2])

for i in range(n-1,2,-1):
    big = dp[i-3] + k
    if dp[i] > big:
        dp[i] = big
        for j in range(i, n):
            dp[j] = min(dp[j], dp[j-1]+s_jump[j-1], dp[j-2]+l_jump[j-2])

print(dp[n-1])



