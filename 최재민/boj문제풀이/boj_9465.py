import sys

T = int(input())
for i in range(T):
    n = int(input())
    stick = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    if n >= 2:
        stick[0][1] += stick[1][0]
        stick[1][1] += stick[0][0]

        for j in range(2, n):
            stick[0][j] += max(stick[1][j-1], stick[1][j-2])
            stick[1][j] += max(stick[0][j-1], stick[0][j-2])
    print(max(stick[0][n-1], stick[1][n-1]))
