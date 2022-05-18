N = int(input())

k = []
cnt = 1

for i in range(N):
    k.append(int(input()))

k.sort(reverse=True)

for i in range(N):
    k[i]=k[i]*(i+1)

print(max(k))
