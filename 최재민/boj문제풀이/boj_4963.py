import sys
sys.setrecursionlimit(10**6)

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    jido = []

    for i in range(h):
        jido.append(list(map(int, input().split())))

    visit = [[0] * w for i in range(h)]

    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]


    def dfs(x, y):
        visit[x][y] = 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if visit[nx][ny] == 0 and jido[nx][ny] == 1:
                    dfs(nx, ny)


    cnt = 0

    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and jido[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)
