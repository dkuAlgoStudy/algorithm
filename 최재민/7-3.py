N,M = map(int,input().split())

duck = list(map(int,input().split()))

start=0
end=max(duck)

while start<=end:
    sum=0
    mid=(start+end)//2
    for i in duck:
        if i>mid:
            sum += i-mid
    if sum<M:
        end=mid-1
    else:
        answer = mid
        start = mid+1

print(answer)


