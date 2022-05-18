a, b = map(int, input().split())
cnt = 1

while True:
    if a == b:
        break
    elif b < a or b % 2 != 0 and b % 10 != 1:
        cnt = -1
        break
    elif b % 10 == 1:
        b //= 10
        cnt += 1
    elif b % 2 == 0:
        b //= 2
        cnt += 1

print(cnt)
