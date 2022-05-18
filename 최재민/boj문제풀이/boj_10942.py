import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())

dp =[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for i in range(2, N):
    for j in range(N-i):
        if arr[j] == arr[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[start-1][end-1])
