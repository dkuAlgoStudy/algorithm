list1 = []
for _ in range(28):
    list1.append(int(input()))

for i in range(1, 31):
    if i not in list1:
        print(i)
