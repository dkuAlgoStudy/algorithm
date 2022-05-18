import sys

n, k = map(int, input().split())
cnt = 0
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)

for i in coin:
    if i <= k:
        cnt += k//i
        k %= i

print(cnt)
