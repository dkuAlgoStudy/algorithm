sum=1
for _ in range(3):
    i=int(input())
    sum*=i

for j in range(10):
    print(str(sum).count(str(j)))
