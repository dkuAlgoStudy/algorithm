N = int(input())
apt = []

visit = [[0]*N for _ in range(N)]

for _ in range(N):
    apt.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, num):
    visit[x][y] = 1
    global cnt

    if apt[x][y] == 1:
        apt[x][y] = num
        cnt += 1

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if visit[nx][ny] == 0 and apt[nx][ny] == 1:
                dfs(nx, ny, num)


dan = 1
aptnum = []
cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 and apt[i][j] == 1:
            dfs(i, j, dan)
            aptnum.append(cnt)
            cnt = 0
            dan += 1

print(len(aptnum))
for i in sorted(aptnum):
    print(i)
