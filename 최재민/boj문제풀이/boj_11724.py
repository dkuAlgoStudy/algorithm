from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[0] for _ in range(N+1)]
visited = [0] * (N+1)


def bfs():
    q = deque()
    cnt = 0
    for i in range(1,N+1):
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)
            cnt += 1
            while q:
                a = q.popleft()
                for j in graph[a]:
                    if visited[j] == 0:
                        visited[j] = 1
                        q.append(j)
    print(cnt)


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
bfs()
