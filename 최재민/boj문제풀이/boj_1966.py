import sys
from collections import deque
TC = int(sys.stdin.readline().rstrip())

for _ in range(TC):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1 

        if best == front:
            count += 1 
            if m < 0: 
                print(count)
                break

        else:   
            queue.append(front) 
            if m < 0 :  
                m = len(queue) - 1 