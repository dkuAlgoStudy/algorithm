import sys

n = int(input())
stud = [[0] for _ in range((n**2)+1)]
seat = [[0]*n for _ in range(n)]
priority = []
x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

for _ in range(n**2):
    b = list(map(int, sys.stdin.readline().split()))
    priority.append(b[0])
    stud[b[0]] = b[1:]

answer = 0

for p in priority:
    a = []
    for i in range(n):
        for j in range(n):
            if seat[i][j] == 0:
                cnt = 0
                cnt2 = 0
                big = 0
                big2 = 0
                for k in range(4):
                    dx = i + x[k]
                    dy = j + y[k]
                    if 0 <= dx < n and 0 <= dy < n:
                        if seat[dx][dy] in stud[p]:
                            cnt += 1
                        if seat[dx][dy] == 0:
                            cnt2 += 1
                if cnt > big or (cnt == big and cnt2 >= big2):
                    big = cnt
                    big2 = cnt2
                    a.append([big, big2, i, j])

    a = sorted(a, key=lambda x : (-x[0], -x[1], x[2]))

    q = 0

    while seat[a[q][2]][a[q][3]] != 0:
        if len(a)-1 == q:
            break
        q += 1
    seat[a[q][2]][a[q][3]] = p


for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            dx = i + x[k]
            dy = j + y[k]
            if 0 <= dx < n and 0 <= dy < n:
                if seat[dx][dy] in stud[seat[i][j]]:
                    cnt += 1
        if cnt >= 1:
            answer += 10**(cnt-1)

print(answer)
