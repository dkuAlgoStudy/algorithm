import sys

n, m = map(int, input().split())

arr = sys.stdin.readline().rstrip()
answer = sys.stdin.readline().rstrip()


dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


def correct(a, b):
    if a == b:
        return True
    elif a == "i" and (b == 'i' or b == 'j' or b == 'l'):
        return True
    elif a == "v" and (b == "v" or b == "w"):
        return True
    else:
        return False


for i in range(1, n+1):
    dp[i][0] = i
for i in range(1, m+1):
    dp[0][i] = i

for i in range(1, n+1):
    for j in range(1, m+1):
        if correct(arr[i-1], answer[j-1]):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

print(dp[n][m])