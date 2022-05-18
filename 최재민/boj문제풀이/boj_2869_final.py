A,B,V=map(int,input().split())
    #if(A*cnt-B*(cnt-1)>=V):
    #cnt를 최소화 해야하기 때문에 부등식을 아래와 같이 cnt에 관해 고칠 수 있음
    #cnt>=(V-B)/(A-B)

cnt=(V-B)/(A-B)
if cnt!=int(cnt):
    cnt=int(cnt)+1

print(int(cnt))

