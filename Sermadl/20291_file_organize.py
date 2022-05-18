n = int(input())

files = []
for i in range(n):
    files.append(list(map(str, input().split('.'))))
files.sort(key = lambda x:(x[1], x[0]))

a = files[0][1]
checked = {files[0][1]: 0}
for i, j in files:
    if a != j:
        checked[j] = 1
        a = j
    else:
        checked[j] += 1
for key, value in checked.items():
    print(key, value)