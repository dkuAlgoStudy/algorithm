import sys

n = int(input())
cow = [[0] for _ in range(11)]
cross = 0

for _ in range(n):
    num, state = map(int, sys.stdin.readline().split())
    cow[num].append(state)

for i in range(1, 11):
    for j in range(2, len(cow[i])):
        if cow[i][j] != cow[i][j-1]:
            cross += 1

print(cross)