n = int(input())

Red_B = list(map(int,input().split()))

Red_B.sort(reverse=True)
answer = Red_B[0]

for i in range(1,n):
    answer += Red_B[i]/2

print(round(answer,4))
