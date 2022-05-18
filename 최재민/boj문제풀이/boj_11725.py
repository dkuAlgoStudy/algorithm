import sys

n = int(input())

graph = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]

for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph, parent):
    queue = [1]
    while queue:
        n = queue.pop()
        for i in graph[n]:
            parent[i].append(n)
            queue.append(i)
            graph[i].remove(n)
    return parent


for i in list(dfs(graph, parent))[2:n+1]:
    print(i[0])
