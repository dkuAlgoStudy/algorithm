N, M = map(int, input().split())

max_card=0

for i in range(N):
    card=list(map(int, input().split()))
    min_card=min(card)
    max_card=max(min_card,max_card)

print(max_card)