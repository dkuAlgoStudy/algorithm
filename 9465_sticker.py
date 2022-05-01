import sys

T = int(input())

for i in range(T):
    n = int(input())
    sticker = []
    for j in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    for k in range(1, n):
        if k == 1:
            sticker[0][k] += sticker[1][k-1]
            sticker[1][k] += sticker[0][k-1]
        else:
            sticker[0][k] += max(sticker[1][k-1], sticker[1][k-2])
            sticker[1][k] += max(sticker[0][k-1], sticker[0][k-2])
    print(max(sticker[0][n-1], sticker[1][n-1]))