N = int(input())

rice = [0]
for i in range(N):
    rice.append(int(input()))
rice += [0]
dp = [[0] * (N+2) for _ in range(N+2)]
ans = []

for right in range(1, N+2):
    for left in range(1, right+1):
        dp[left][N-right+left] = max(dp[left-1][N-right+left] + rice[left-1] * (right-1),
                                     dp[left][N-right+left+1] + rice[N-right+left+1] * (right-1))
        if right-1 == N:
            ans.append(dp[left][N-right+left])
print(max(ans))
