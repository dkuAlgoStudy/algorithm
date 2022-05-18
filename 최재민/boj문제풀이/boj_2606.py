com = int(input())
N = int(input())

computer = [[] for _ in range(com + 1)]
Visited = [False] * (com + 1)

for _ in range(N):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)


def dfs(Graph, v, Visited):
    Visited[v] = True

    for i in Graph[v]:
        if Visited[i] is False:
            global num
            num += 1
            dfs(Graph, i, Visited)


num = 0

dfs(computer, 1, Visited)

print(num)
