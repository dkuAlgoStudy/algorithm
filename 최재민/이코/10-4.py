import copy
from collections import deque

n = int(input())

indegree =[0]*(n+1)
graph = [[]for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1,n+1):
    a = list(map(int, input().split()))
    time[i] = a[0]
    for j in a[1:-1]:
        graph[j].append(i)
        indegree[i]+=1

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            result[i] += time[now]
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])

topology_sort()