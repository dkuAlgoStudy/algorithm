import sys


def set_direct(dir, cnt, move, length):
    cnt += 1
    if cnt == length:
        dir = (dir + 1) % 4
        cnt = 0
        move += 1
        if move % 2 == 0:
            length += 1
            move = 0
    return dir, cnt, move, length


def move_marble(cx, cy):
    global marble
    x, y = cx, cy
    marbles = []
    direct, cnt, move, length = 0, 0, 0, 1
    while True:
        nx = x + dx1[direct]
        ny = y + dy1[direct]
        if marble[nx][ny] != 0:
            marbles.append(marble[nx][ny])

        x, y = nx, ny
        if x == 0 and y == 0:
            break
        direct, cnt, move, length = set_direct(direct, cnt, move, length)
    marble = [[0] * n for _ in range(n)]
    x, y = cx, cy
    direct, cnt, move, length = 0, 0, 0, 1

    for k in marbles:
        nx = x + dx1[direct]
        ny = y + dy1[direct]
        marble[nx][ny] = k

        x, y = nx, ny
        direct, cnt, move, length = set_direct(direct, cnt, move, length)


def pop_marble(cx, cy):
    global answer
    x, y = cx, cy
    marbles = []
    direct, cnt, move, length = 0, 0, 0, 1
    poped = 0
    while True:
        if len(marbles) == 0:
            marbles.append([x, y])
        nx = x + dx1[direct]
        ny = y + dy1[direct]
        if marble[nx][ny] == marble[x][y]:
            marbles.append([nx, ny])
            if nx == 0 and ny == 0:
                if len(marbles) >= 4:
                    poped = 1
                    for i, j in marbles:
                        if marble[i][j] == 1:
                            answer += 1
                        elif marble[i][j] == 2:
                            answer += 2
                        elif marble[i][j] == 3:
                            answer += 3
                        marble[i][j] = 0

        elif marble[nx][ny] != marble[x][y]:
            if len(marbles) >= 4:
                poped = 1
                for i, j in marbles:
                    if marble[i][j] == 1:
                        answer += 1
                    elif marble[i][j] == 2:
                        answer += 2
                    elif marble[i][j] == 3:
                        answer += 3
                    marble[i][j] = 0
            marbles = []
        x, y = nx, ny
        if (x == 0 and y == 0) or marble[x][y] == 0:
            return poped

        direct, cnt, move, length = set_direct(direct, cnt, move, length)


n, m = map(int, input().split())
marble = []
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dx1 = [0, 1, 0, -1]
dy1 = [-1, 0, 1, 0]
for _ in range(n):
    marble.append(list(map(int, sys.stdin.readline().split())))

center_x, center_y = n//2, n//2


for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    d -= 1

    for i in range(1, s + 1):
        nx = center_x + i * dx[d]
        ny = center_y + i * dy[d]
        if not 0 <= nx < n or not 0 <= ny < n:
            break
        marble[nx][ny] = 0

    while True:
        move_marble(center_x, center_y)
        poped = pop_marble(center_x,center_y)
        if poped == 0:
            break
    x, y = center_x, center_y-1
    direct, cnt, move, length = 1, 0, 1, 1
    group = 0
    changed = []
    group_cnt = 0
    while True:
        if group == 0:
            group_num = marble[x][y]
            group_cnt = 1
            group = 1

        nx = x + dx1[direct]
        ny = y + dy1[direct]
        if marble[nx][ny] == marble[x][y]:
            group_cnt += 1
            if nx == 0 and ny == 0:
                changed.append(group_cnt)
                changed.append(group_num)

        else:
            changed.append(group_cnt)
            changed.append(group_num)
            group = 0

        x, y = nx, ny
        if (x == 0 and y == 0) or marble[x][y] == 0:
            break
        direct, cnt, move, length = set_direct(direct, cnt, move, length)
    x, y = center_x, center_y
    direct, cnt, move, length = 0, 0, 0, 1
    marble = [[0] * n for _ in range(n)]

    if changed:
        for k in changed:
            nx = x+dx1[direct]
            ny = y+dy1[direct]
            marble[nx][ny] = k

            x, y = nx, ny
            if (x == 0 and y == 0) or marble[x][y] == 0:
                break
            direct, cnt, move, length = set_direct(direct, cnt, move, length)

print(answer)
