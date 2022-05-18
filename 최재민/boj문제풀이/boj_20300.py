n = int(input())

muscle = list(map(int, input().split()))
m = 0

muscle.sort()

if len(muscle) % 2 == 0:
    for i in range(n//2):
        m = max(m, muscle[i]+muscle[n-1-i])
else:
    for i in range(n//2):
        m = max(m, muscle[i]+muscle[n-i-2])
    m = max(m, muscle[-1])

print(m)