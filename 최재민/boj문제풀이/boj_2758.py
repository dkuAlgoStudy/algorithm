t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    dp = [[0]*(m+1) for _ in range(n)]

    for i in range(m+1):
        dp[0][i] = i

    for i in range(1, n):
        for j in range(2 ** i,m+1):
            dp[i][j] = dp[i-1][j//2] + dp[i][j-1]
    print(dp[n-1][m])


