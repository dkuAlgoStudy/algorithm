from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    result = 0
    while q:
        result += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if tomato[nx][ny] == 0:
                        tomato[nx][ny] = 1
                        q.append([nx, ny])
    return result


M, N = map(int, input().split())
tomato, q = [], deque()
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            q.append([i, j])
    tomato.append(row)

result = bfs() - 1

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()

print(result)
