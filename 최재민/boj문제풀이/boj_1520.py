import sys
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = []
dp = [[-1] * m for _ in range(n)]
dp[n-1][m-1] = 1
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[x][y] > graph[nx][ny]:
            temp += dfs(nx, ny)
    dp[x][y] = temp
    return dp[x][y]


print(dfs(0, 0))

