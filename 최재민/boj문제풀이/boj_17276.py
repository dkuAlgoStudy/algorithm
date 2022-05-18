import sys


def turn(array, n):
    center = n // 2
    for i in range(n):
        array[i][i], array[i][center] = array[i][center], array[i][i]
        array[i][i], array[i][n - 1 - i] = array[i][n - 1 - i], array[i][i]
        array[i][i], array[center][i] = array[center][i], array[i][i]

    for i in range(center):
        array[center][i], array[center][n - 1 - i] = array[center][n - 1 - i], array[center][i]

    return array


t = int(input())

for _ in range(t):
    n, angle = map(int, input().split())
    array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    cnt = angle // 45
    if cnt < 0:
        cnt += 8

    for _ in range(cnt):
        array = turn(array, n)

    for i in range(n):
        for j in range(n):
            print(array[i][j], end=' ')
        print()

