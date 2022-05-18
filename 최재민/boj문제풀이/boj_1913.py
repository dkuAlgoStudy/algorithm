def set_graph(dir, cnt, move, length):
    cnt += 1
    if cnt == length:
        dir = (dir + 1) % 4
        cnt = 0
        move += 1
        if move % 2 == 0:
            length += 1
            move = 0
    return dir, cnt, move, length


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]

x, y = n//2, n//2
direct, cnt, move, length = 0, 0, 0, 1

for i in range(1, n**2+1):
    graph[x][y] = i
    if graph[x][y] == m:
        answer_x = x
        answer_y = y
    x += dx[direct]
    y += dy[direct]

    direct, cnt, move, length = set_graph(direct, cnt, move, length)

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(graph[i][j])
            break
        print(graph[i][j], end=" ")

print(answer_x+1, answer_y+1)


