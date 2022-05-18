N, K = map(int, input().split())

table = input()
table = list(table)
cnt = 0

for i in range(len(table)):
    if table[i] == "P":
        for j in range(i - K, i + K + 1):
            if 0 <= j < N and table[j] == 'H':
                cnt += 1
                table[j] = "X"
                break

print(cnt)

