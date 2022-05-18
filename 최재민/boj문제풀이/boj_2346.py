from collections import deque
import sys
N = int(sys.stdin.readline())
a = deque(enumerate(map(int, sys.stdin.readline().split())))

result = []
while a:
    num, i = a.popleft()
    result.append(num+1)
    if i > 0:
        a.rotate(-(i-1))
    else:
        a.rotate(-i)
for j in result:
    print(j, end = ' ')
