import sys

n = int(input())
marble = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

dp = [0] * (2 * 40000 + 1)
dp[40000] = 1

for i in marble:
    temp = dp[:]
    for j in range(-40000, 40000+1):
        if dp[j+40000] == 0:
            continue
        if j-i >= -40000:
            temp[j-i+40000] = 1
        if j+i <= 40000:
            temp[j+i+40000] = 1
    dp = temp[:]
for i in check:
    if dp[i+40000] == 1:
        print('Y', end=" ")
    else:
        print('N', end=" ")
