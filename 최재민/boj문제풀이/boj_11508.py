import sys

n = int(input())

milk = []

answer = 0

for i in range(n):
    milk.append(int(sys.stdin.readline().rstrip()))

milk.sort(reverse=True)

for i in range(n):
    if i % 3 == 2:
        continue
    answer += milk[i]

print(answer)


