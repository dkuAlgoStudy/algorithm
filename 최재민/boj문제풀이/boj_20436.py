import sys

left = ['qwert', 'asdfg', 'zxcv']
right = ['0yuiop', '0hjkl', 'bnm']

l_hand, r_hand = sys.stdin.readline().split()
zoac = sys.stdin.readline().rstrip()

left_x, left_y, right_x, right_y = 0, 0, 0, 0

for i in range(3):
    if l_hand in left[i]:
        left_x = i
        left_y = left[i].index(l_hand)

for i in range(3):
    if r_hand in right[i]:
        right_x = i
        right_y = right[i].index(r_hand)

time = 0

for i in zoac:
    for j in range(3):
        if i in left[j]:
            time += abs(left_x-j) + abs(left_y-left[j].index(i))
            left_x = j
            left_y = left[j].index(i)
            time += 1
    for r in range(3):
        if i in right[r]:
            time += abs(right_x - r) + abs(right_y - right[r].index(i))
            right_x = r
            right_y = right[r].index(i)
            time += 1

print(time)
