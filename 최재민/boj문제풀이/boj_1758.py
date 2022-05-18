import sys

N = int(input())

custom=[]
answer=0

for _ in range(N):
    custom.append(int(sys.stdin.readline().rstrip()))

custom.sort(reverse=True)

for i in range(N):
    tip = custom[i]-i

    if tip > 0:
        answer += tip

print(answer)
