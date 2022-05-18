import sys

n, k = map(int,input().split())

height = list(map(int, sys.stdin.readline().split()))
ans = 0

diff = []
for i in range(1, n):
    diff.append(height[i]-height[i-1])

diff.sort()

if k == n:
    print(0)
else:
    print(sum(diff[0:n-k]))
