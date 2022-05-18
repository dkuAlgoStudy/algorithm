def solution(costs, xcosts, ycosts):
    answer = -1
    dp = [[0 for _ in range(len(costs[0])+2)]for i in range(len(costs)+2)]
    for i in range(1, len(costs)+1, 1):
        for j in range(1, len(costs[0]) + 1):
            if i == 1 and j == 1:
                dp[i][j] = costs[i-1][j-1]
            elif j == 1:
                dp[i][j] = dp[i-1][j]+costs[i-1][j-1]-ycosts
            elif i == 1:
                dp[i][j] = dp[i][j-1]+costs[i-1][j-1]-xcosts
            else:
                dp[i][j] = max(dp[i - 1][j]-ycosts, dp[i][j - 1]-xcosts) + costs[i-1][j-1]
    return (max(dp[len(costs)]))

print(solution([[1, 2, 3],[4, 5, 6],[7,8,9]],100,0))