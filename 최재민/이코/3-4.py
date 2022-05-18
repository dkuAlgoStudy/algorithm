N, K = map(int, input().split())
answer = 0

while N>=K:
    while N % K != 0:
        N-=1
        answer += 1

    N//=K
    answer+=1

while N > 1:
    N-=1
    answer +=1

print(answer)