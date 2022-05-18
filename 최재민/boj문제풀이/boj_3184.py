from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(x, y):
    global sheep, wolf
    q = deque()
    q.append([x, y])
    o, v = 0, 0
    if farm[x][y] == "o":
        o += 1
    elif farm[x][y] == "v":
        v += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if visited[nx][ny] == 0 and farm[nx][ny] != "#":
                    if farm[nx][ny] == "o":
                        o += 1
                    if farm[nx][ny] == "v":
                        v += 1
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    if o > v:
        sheep += o
    if v >= o:
        wolf += v


R, C = map(int, input().split())
farm = []
visited = [[0]*C for _ in range(R)]

sheep = 0
wolf = 0

for i in range(R):
    a = list(input().strip())
    farm.append(a)
for i in range(R):
    for j in range(C):
        if (farm[i][j] == "o" or farm[i][j] == "v") and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)

print(sheep, wolf)
