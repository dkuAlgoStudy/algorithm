import sys

n = int(input())

dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

bomb = []
none = []

for _ in range(n):
    bomb.append(list(sys.stdin.readline().rstrip()))
for _ in range(n):
    none.append(list(sys.stdin.readline().rstrip()))

# 지뢰가 있는 칸이 열려있는지 확인하는 변수
flag = 0

for i in range(n):
    for j in range(n):
        count = 0
        if none[i][j] == 'x':
            if bomb[i][j] == '*':
                flag = 1
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if bomb[nx][ny] == '*':
                        count += 1
            none[i][j] = count

if flag == 1:
    for a in range(n):
        for b in range(n):
            if bomb[a][b] == '*':
                none[a][b] = '*'


for i in range(n):
    for j in range(n):
        if j == n - 1:
            print(none[i][j])
        else:
            print(none[i][j], end="")
