import sys

n, m = map(int,input().split())
flight = [[0 for _ in range(m+2)] for _ in range(n+2)]
dp1 = [[-1e9 for _ in range(m+2)] for _ in range(n+2)]
dp2 = [[-1e9 for _ in range(m+2)] for _ in range(n+2)]

for i in range(1, n+1):
    flight[i][1:m+1] = list(map(int, sys.stdin.readline().split()))


for i in range(n, 0, -1):
    for j in range(1, m+1):
        if i == n and j == 1:
            dp1[i][j] = flight[i][j]
        else:
            dp1[i][j] = max(dp1[i+1][j], dp1[i][j-1])+flight[i][j]

for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        if i < n and j < m:
            dp2[i][j] = max(dp2[i+1][j], dp2[i][j+1])+flight[i][j]
        elif i < n:
            dp2[i][j] = dp2[i+1][j] + flight[i][j]
        elif j < m:
            dp2[i][j] = dp2[i][j+1] + flight[i][j]
        else:
            dp2[i][j] = flight[i][j]
answer = int(-1e18)
for i in range(1, n+1):
    for j in range(1, m+1):
        answer = max(answer, dp1[i][j] + dp2[i][j])

print(answer)

