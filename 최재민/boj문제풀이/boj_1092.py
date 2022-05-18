import sys

input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse = True)
box.sort(reverse = True)

time = 0 
moved = [0 for _ in range(m)] 
count = 0 

positions = [0] * n

if max(box) > max(crane):
    print(-1)

else:
    while count < len(box):
        for i in range(n): 
            while positions[i] < len(box):
                if not moved[positions[i]] and crane[i] >= box[positions[i]]:
                    moved[positions[i]] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        time += 1
    print(time)    
             