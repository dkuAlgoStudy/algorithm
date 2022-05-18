n = int(input())

road = list(map(int, input().split()))
oil = list(map(int, input().split()))

answer = 0
m = oil[0]

for i in range(n-1):
    if oil[i] < m:
        m = oil[i]
    answer += m * road[i]

print(answer)
