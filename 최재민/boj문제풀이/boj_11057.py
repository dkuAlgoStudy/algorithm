N = int(input())
length = ([[1]*10])
for _ in range(N):
    length.append(list([0]*10))

for i in range(1, N+1):
    for j in range(10):
        for k in range(j+1):
            length[i][j] += length[i-1][k]

print(length[N][9]%10007)


