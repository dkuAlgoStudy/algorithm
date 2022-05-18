import sys

concave = []
answer = []

dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]
for _ in range(19):
    concave.append(list(map(int, sys.stdin.readline().split())))

for i in range(19):
    for j in range(19):
        if concave[i][j] != 0:
            x = i
            y = j
            for k in range(8):
                nx = x
                ny = y
                cnt = 1
                while True:
                    nx = nx + dx[k]
                    ny = ny + dy[k]
                    if 0 <= nx < 19 and 0 <= ny < 19:
                        if concave[nx][ny] == concave[x][y]:
                            cnt += 1
                        else:
                            break
                    else:
                        break
                if cnt == 5:
                    if 0 <= x-dx[k] < 19 and 0 <= y-dy[k] < 19:
                        if concave[x][y] != concave[x-dx[k]][y-dy[k]]:
                            answer.append([i, j])
                    else:
                        answer.append([i, j])

answer = sorted(answer, key=lambda x: (x[1], x[0]))
if answer:
    print(concave[answer[0][0]][answer[0][1]])
    print(answer[0][0] + 1, answer[0][1] + 1)
else:
    print(0)
