import sys

n, m = map(int, input().split())

light = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        light[b-1] = c
    if a == 2:
        for i in range(b-1, c):
            if light[i] == 0:
                light[i] = 1
            elif light[i] == 1:
                light[i] = 0
    if a == 3:
        for i in range(b-1, c):
            light[i] = 0
    if a == 4:
        for i in range(b-1, c):
            light[i] = 1

for i in light:
    print(i, end=" ")
