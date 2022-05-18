h, w = map(int, input().split())
block = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left = max(block[:i])
    right = max(block[i+1:])

    compare = min(left, right)
    if block[i] < compare:   
        ans += compare - block[i]
print(ans)

