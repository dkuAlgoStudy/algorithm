import sys
import time

n, k = map(int, sys.stdin.readline().split())

num = list(input())
answer = []
temp = k
for i in range(n):
    while temp > 0 and answer:
        if answer[-1] < num[i]:
            answer.pop()
            temp -= 1
        else:
            break
    answer.append(num[i])

print(''.join(answer[:n-k]))
