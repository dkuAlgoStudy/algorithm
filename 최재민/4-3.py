N, M = map(int, input().split())

x, y, a = map(int, input().split())
visitmap = []
map1 = []
for _ in range(N):
    visitmap.append([0] * M)
for _ in range(N):
    map1.append(list(map(int, input().split())))

visitmap[x][y] = 1
count = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn = 0

while (True):
    a -= 1
    if a == -1:
        a = 3
    nx = x + dx[a]
    ny = y + dy[a]

    if visitmap[nx][ny] == 0 and map1[nx][ny] == 0:
        visitmap[nx][ny] = 1
        x = nx
        y = ny
        turn = 0
        count += 1

    else:
        turn += 1

    if turn == 4:
        nx = x - dx[a]
        ny = y - dy[a]

        if map1[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(count)
