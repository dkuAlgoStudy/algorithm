import sys

def check_bingo(bingo):
    count = 0
    #가로
    for i in range(5):
        if bingo[i].count(0) == 5:
            count += 1
    #세로
    for j in range(5):
        temp = 0
        for k in range(5):
            if bingo[k][j] == 0:
                temp += 1
        if temp == 5:
            count += 1
    #좌상단 대각
    temp = 0
    for b in range(5):
        if bingo[b][b] == 0:
            temp += 1
    if temp == 5:
        count += 1
    #우상단 대각
    temp = 0
    for c in range(5):
        if bingo[c][4-c] == 0:
            temp += 1
    if temp == 5:
        count += 1

    return count


bingo = []
mc = []
answer = 0

for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))

for _ in range(5):
    mc.append(list(map(int, sys.stdin.readline().split())))

cnt1 = 0
cnt2 = 0
win = []

for x in mc:
    while x:
        a = x.pop(0)
        answer += 1
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == a:
                    bingo[i][j] = 0
        if check_bingo(bingo) >= 3:
            win.append(answer)
            break

print(min(win))





