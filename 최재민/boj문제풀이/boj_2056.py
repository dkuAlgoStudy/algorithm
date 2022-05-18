from collections import deque
from collections import defaultdict
from copy import deepcopy

n = int(input())
indegree = [0] * (n+1)
graph = defaultdict(list)
time = [0] * (n+1)
answer = [0] * (n+1)
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[2:len(data)]:
        indegree[i] += 1
        graph[x].append(i)

dq = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)
        answer[i] = time[i]

while dq:
    now = dq.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        answer[i] = max(answer[i], answer[now] + time[i])
        if indegree[i] == 0:
            dq.append(i)

print(max(answer))
