i = 0
while True:
    i+=1    
    l, p, v = map(int,input().split())
    if l==0:
        break
    answer = 0

    while v >= p:
        v -= p
        answer += l

    if v >= l:
        answer += l
    else : 
        answer += v

    print(f"Case {i}:" ,answer)