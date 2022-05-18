T = int(input())
N=[list(map(int,input().split()))

for _ in range(0,T)]

list=[]

for i in range(1,T):
    for j in range(len(N[i])):
        if j == 0 :
            N[i][j] += (N[i-1][j])
        elif j==i:
            N[i][j] +=(N[i-1][j-1])
        else :
            N[i][j] += (max(N[i-1][j],N[i-1][j-1]))
print(max(N[T-1]))
