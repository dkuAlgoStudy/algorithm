import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
s = input().strip()
m = int(input())
dp = [-1 for _ in range(len(s)+1)]
A = []

for _ in range(m):
    A.append(list(map(str, input().split())))    
    A[-1][1] = int(A[-1][1])

def delText(i):
    global s
    
    if i >= len(s):
        return 0
    if dp[i] != -1:
        return dp[i]
    dp[i] = delText(i+1) + 1

    for string in A:
        if s[i:i+len(string[0])] == string[0]:
            dp[i] = max(dp[i], delText(i+len(string[0])) + string[1])

    return dp[i]

print(delText(0))
