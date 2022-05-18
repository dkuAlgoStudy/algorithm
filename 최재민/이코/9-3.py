import sys
import heapq
input = sys.stdin.readline
N, M, C = map(int, input().split())
INF=int(1e9)

graph = [[] for i in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)
cnt = 0
time = 0

for i in range(1, N+1):
    if distance[i] != INF and distance[i]!=0:
        cnt += 1
        time =max(distance[i],time)

print(cnt, time)
