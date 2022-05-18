import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    cnt = 1

    while q:
        st = q.popleft()
        for i in s[st]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt


s = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    s[b-1].append(a-1)

result = [0 for _ in range(N)]
for i in range(N):
    result[i]=bfs(i)

for i in range(N):
    if result[i]==max(result):
        print(i+1,end=' ')


