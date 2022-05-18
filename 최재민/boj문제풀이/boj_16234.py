from collections import deque
import sys
N, L, R = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    move = deque()
    q.append([x, y])
    visit[x][y] = 1
    people, cnt = 0, 0
    while q:
        x, y = q.popleft()
        move.append([x, y])
        people += graph[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visit[nx][ny] = cnt
                    q.append([nx, ny])

    while move:
        x, y = move.popleft()
        graph[x][y] = people // cnt

    if cnt == 1:
        return 0
    return 1

while True:
    q = deque()
    visit = [[0]*N for _ in range(N)]
    cnt, people = 0, 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                cnt += bfs(i, j)
    if cnt == 0:
        break
    answer += 1

print(answer)

