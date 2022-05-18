N, K = map(int, input().split())

arr = list(map(int, input().split()))
arr = [0] + arr

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]  #dp[N][K]는 N번째 숫자까지 K번 짤랐을 때

for i in range(1, N+1):
    arr[i] %= 2
    for j in range(0, K+1):
        if arr[i] == 0:
            dp[i][j] = dp[i-1][j]+1
        if j != 0 and arr[i]:
            dp[i][j] = dp[i - 1][j - 1]
ans = []
for i in dp:
    ans.append(i[K])

print(max(ans))