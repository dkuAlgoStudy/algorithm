import sys

N = int(input())

honey = list(map(int, sys.stdin.readline().split()))
h_sum = sum(honey)
answer = [0] * 3
s = []
s.append(honey[0])

for i in range(1, N):
    s.append(s[i-1]+honey[i])

for i in range(1,N-1):  # 양쪽끝에 벌이 있을경우
    answer[0] = max(answer[0], s[N-2]-honey[0]+honey[i])

for i in range(1, N-2):  # 오른쪽끝에 벌
    answer[1] = max(answer[1], s[N-1]-honey[i]-honey[0]+s[N-1]-s[i])


for i in range(1, N-1):  # 왼쪽끝에벌
    answer[2] = max(answer[2], h_sum-honey[i]-honey[N-1]+s[i-1])

print(max(answer))
