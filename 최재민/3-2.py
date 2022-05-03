N,M,K = map(int,input().split())
num = list(map(int,input().split()))

sum = 0
cnt=0

num = sorted(num)
max=num[N-1]
max2=num[N-2]

while cnt<=M:
    for k in range(K):
        if cnt==M:
            break
        sum += max
        cnt += 1
    if cnt==M:
        break
    sum+=max2
    cnt+=1

print(sum)

