calen = [0]*366

n = int(input())
todo = []

for _ in range(n):
    start, end = map(int, input().split(' '))
    for i in range(start,end+1):
        calen[i] += 1

row = 0
col = 0
answer = 0

for i in range(366):
    if calen[i] != 0:
        row = max((row,calen[i]))
        col += 1
    else:
        answer += row * col
        row = 0
        col = 0
answer += row * col

print(answer)