n = int(input())
goal = n
cnt = 0

while True:
    a = goal // 10
    b = goal % 10
    c = (a + b) % 10
    goal = (b * 10) + c

    cnt += 1
    if goal == n :
        break

print(cnt)