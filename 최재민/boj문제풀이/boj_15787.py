import sys

n, m = map(int, input().split())
train = [[0] * 20 for _ in range(n)]

for _ in range(m):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        train[command[1]-1][command[2]-1] = 1
    elif command[0] == 2:
        train[command[1]-1][command[2]-1] = 0
    elif command[0] == 3:
        for i in range(19, 0, -1):
            train[command[1]-1][i] = train[command[1]-1][i-1]
        train[command[1]-1][0] = 0
    else:
        for i in range(0, 19):
            train[command[1]-1][i] = train[command[1]-1][i+1]
        train[command[1]-1][19] = 0

answer = set()

for t in train:
    temp = tuple(t)
    answer.add(temp)

print(len(answer))

