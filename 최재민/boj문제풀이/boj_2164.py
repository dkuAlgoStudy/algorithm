from collections import deque
import imp
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

queue = deque()
for i in range(1,n+1):
    queue.append(i)

while True:
    a = queue.popleft()
    if not queue:
        print(a)
        break
    b = queue.popleft()
    queue.append(b)