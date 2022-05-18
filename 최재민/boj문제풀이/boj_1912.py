n = int(input())
list = list(map(int, input().split()))

sum = [list[0]]
for i in range(len(list)-1):
    sum.append(max(sum[i]+list[i+1], list[i+1]))

