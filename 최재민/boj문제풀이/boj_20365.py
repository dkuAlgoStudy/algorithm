n = int(input())

blog = list(input())

cnt1=1
cnt2=1

if blog[0] == 'R':
    cnt1 += 1
else:
    cnt2 += 1

for i in range(1, n): #파랑으로 칠함
    if blog[i] == 'R':
        cnt1 += 1
        if blog[i-1] == 'R':
            cnt1 -= 1

for i in range(1, n):    #빨강으로 칠함
    if blog[i] == 'B':
        cnt2 += 1
        if blog[i-1] =='B':
            cnt2 -= 1

if n == 1:
    print(1)
else:
    print(min(cnt1, cnt2))
