import sys

V = int(sys.stdin.readline())

matrix = [[] for _ in range(V + 1)]

for _ in range(V):
    path = list(map(int, sys.stdin.readline().split()))
    path_len = len(path)
    for i in range(1, path_len // 2):
        matrix[path[0]].append([path[2 * i - 1], path[2 * i]])

result1 = [0 for _ in range(V + 1)]


def DFS(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            DFS(e, matrix, result)


DFS(1, matrix, result1)
result1[1] = 0

tmpmax = 0
index = 0

for i in range(len(result1)):
    if tmpmax < result1[i]:
        tmpmax = result1[i]
        index = i

result2 = [0 for _ in range(V + 1)]
DFS(index, matrix, result2)
result2[index] = 0
print(max(result2))
