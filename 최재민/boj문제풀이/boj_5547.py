from collections import deque

ox = [-1, -1, -1,  0,  1,  0]
oy = [-1,  0,  1,  1,  0, -1]
#홀수헹

ex = [0, -1,  0,  1,  1,  1]
ey = [-1,  0,  1,  1,  0, -1]
#짝수행

answer = 0


def bfs(x, y):
    global answer
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if x % 2 != 0:
            for i in range(6):
                nx = x + ex[i]
                ny = y + ey[i]
                if 0 <= nx <= h+1 and 0 <= ny <= w+1:
                    if graph[nx][ny] == 0:
                        q.append([nx, ny])
                        graph[nx][ny] = -1
                    elif graph[nx][ny] == 1:
                        answer += 1
                        print(x,y,ex[i],ey[i])
        else:
            for i in range(6):
                nx = x + ox[i]
                ny = y + oy[i]
                if 0 <= nx <= h + 1 and 0 <= ny <= w + 1:
                    if graph[nx][ny] == 0:
                        q.append([nx, ny])
                        graph[nx][ny] = -1
                    elif graph[nx][ny] == 1:
                        answer += 1
                        print(x, y, ox[i], oy[i])
    return answer


w, h = map(int, input().split())

graph = [[0]*(w+2) for _ in range(h+2)]

for i in range(1, h+1):
    graph[i][1:w+1] = list(map(int, input().split()))
for i in range(h+2):
    if i % 2 == 1:
        print("  ", end = '')
    print(graph[i])

print(bfs(0, 0))