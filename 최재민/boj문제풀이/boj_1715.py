import heapq
n = int(input())
ans = 0
card = []

for i in range(n):
    heapq.heappush(card, int(input()))

while len(card) > 1:
    min1 = heapq.heappop(card)
    min2 = heapq.heappop(card)
    ans += min1 + min2
    heapq.heappush(card, ans)

print(ans)