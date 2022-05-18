t = int(input())
for i in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    answer = int(input())
    dp = [0] * (answer+1)
    dp[0] = 1

    for l in coin:
        for k in range(1, answer + 1):
            if k-l >= 0:
                dp[k] += dp[k-l]
    print(dp[answer])
