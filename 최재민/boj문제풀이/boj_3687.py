import sys

t = int(input())
mini = ['1', '7', '4', '2', '0', '8']
dp = [0, 0, 1, 7, 4, 2, 6, 8, 10]
dp += [1000000000000000000000] * 92


def getmax(n):
    if n % 2 == 0:
        arr = '1' * (n//2)
    else:
        arr = '7' + '1'*(n//2 - 1)
    print(arr, end=" ")


def getmin(n):
    for i in range(9, 101):
        for j in range(2, 8):
            now = str(dp[i-j]) + mini[j-2]
            dp[i] = min(dp[i], int(now))
    print(dp[n], end=' ')


for i in range(t):
    n = int(sys.stdin.readline())
    getmin(n)
    getmax(n)
    if i != t-1:
        print("")
