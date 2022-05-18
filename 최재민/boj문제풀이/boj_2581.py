import math

m = int(input())
n = int(input())
ans = 0
arr = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1
mini = 10001
if m == 1:
    m += 1
for i in range(m, n + 1):
    if arr[i]:
        ans += i
        if i < mini:
            mini = i

if ans == 0:
    print("-1")
else:
    print(ans)
if mini != 10001:
    print(mini)
