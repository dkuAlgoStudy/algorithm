N = int(input())
A = list(map(int, input().split()))

list = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            if list[i] < list[j]:
                list[i] = list[j]
    list[i] += 1

print(max(list))
