import sys

n, m, r = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

for _ in range(r):
    for i in range(min(n, m) // 2):
        start_x, start_y = i, i
        next_num = array[start_x][start_y]

        for j in range(i + 1, n - i):
            start_x = j
            prev = array[start_x][start_y]
            array[start_x][start_y] = next_num
            next_num = prev

        for j in range(i + 1, m - i):
            start_y = j
            prev = array[start_x][start_y]
            array[start_x][start_y] = next_num
            next_num = prev

        for j in range(i + 1, n - i):
            start_x = n - j - 1
            prev = array[start_x][start_y]
            array[start_x][start_y] = next_num
            next_num = prev

        for j in range(i + 1, m - i):
            start_y = m - j - 1
            prev = array[start_x][start_y]
            array[start_x][start_y] = next_num
            next_num = prev

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()