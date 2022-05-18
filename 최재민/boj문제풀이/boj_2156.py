N = int(input())
wine = []
dp = [0 for _ in range(N)]

for _ in range(N):
    wine.append(int(input()))

if N == 1:
    dp[0] = wine[0]
elif N == 2:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(dp[1], wine[2] + wine[0], wine[2] + wine[1])

for i in range(3, N):
    dp[i] = max(max(wine[i] + wine[i-1] + dp[i-3],
                    wine[i] + dp[i-2]), dp[i-1])

print(dp[N-1])