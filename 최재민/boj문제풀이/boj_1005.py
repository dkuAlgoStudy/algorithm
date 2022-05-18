import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    build = [0] + list(map(int, sys.stdin.readline().split()))
    graph = [[]for _ in range(n+1)]
    indeg = [0] * (n+1)
    dp = [0] * (n+1)

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        indeg[b] += 1
        graph[a].append(b)
    q = deque()
    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)
            dp[i] = build[i]
    while q:
        now = q.popleft()
        for i in graph[now]:
            indeg[i] -= 1
            dp[i] = max(dp[now] + build[i], dp[i])
            if indeg[i] == 0:
                q.append(i)
    answer = int(sys.stdin.readline())
    print(dp[answer])

