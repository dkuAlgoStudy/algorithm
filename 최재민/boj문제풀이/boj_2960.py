N, K = map(int, input().split())

arr = [False for _ in range(N + 2)]
cnt = 0
for i in range(2, N + 1):
    if arr[i] == False:
        for j in range(i, N + 1, i):
            if arr[j] == False:
                arr[j] = True
                cnt += 1

                if cnt == K:
                    print(j)
                    break