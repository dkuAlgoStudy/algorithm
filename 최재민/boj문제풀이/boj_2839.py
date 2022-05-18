x = int(input())

answer = 0
while x >= 0:
    if x%5 == 0:
        answer += x//5
        print(answer)
        break
    x -= 3
    answer += 1
else:
    print(-1)

