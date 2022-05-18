import sys

n, m, x, y, k = map(int, input().split())

arr = [[] * m for _ in range(n)]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

order = list(map(int, sys.stdin.readline().split()))

dice = {'top': 0, 'bottom': 0, 'up': 0, 'down': 0, 'right': 0, 'left':0}

for i in order:
    if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
        x += dx[i]
        y += dy[i]
        if i == 1:
            dice['top'], dice['left'],dice['bottom'], dice['right'] = dice['left'], dice['bottom'], dice['right'], dice['top']
        elif i == 2:
            dice['top'], dice['right'],dice['bottom'], dice['left'] = dice ['right'], dice['bottom'], dice['left'], dice['top']
        elif i == 3:
            dice['top'], dice['up'],dice['bottom'],dice['down'] = dice['down'], dice['top'],dice['up'],dice['bottom']
        else:
            dice['top'], dice['down'],dice['bottom'],dice['up'] = dice['up'],dice['top'],dice['down'],dice['bottom']
        if arr[x][y] == 0:
            arr[x][y] = dice['bottom']
        else:
            arr[x][y], dice['bottom'] = dice['bottom'], arr[x][y]
            arr[x][y] = 0
        print(dice['top'])
