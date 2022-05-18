n = int(input())
k = int(input())

high = list(map(int, input().split()))

high.sort()
if n <= k:
    print(0)
else:
    distance = []
    for i in range(n-1):
        distance.append(high[i+1]-high[i])

    distance.sort()
    for i in range(k-1):
        distance.pop()

    print(sum(distance))