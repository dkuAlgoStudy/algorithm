import sys

n = int(input())
switch = list(map(int, sys.stdin.readline().split()))

stud = int(input())

for _ in range(stud):
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1:
        for i in range(n):
            if (i+1) % num == 0:
                if switch[i] == 1:
                    switch[i] = 0
                else:
                    switch[i] = 1

    if sex == 2:
        if num == 1 or num == n:
            num -= 1
        else:
            num -= 1
            index = 1
            while True:
                if num-index < 0 or num+index > n-1:
                    break
                if switch[num-index] == switch[num+index]:
                    if switch[num-index] == 1:
                        switch[num-index], switch[num+index] = 0, 0
                    else:
                        switch[num-index], switch[num+index] = 1, 1
                else:
                    break
                index += 1

        if switch[num] == 1:
            switch[num] = 0
        else:
            switch[num] = 1

for x in range(n):
    
    if (x+1) % 20 == 0:
        print(switch[x])
    else:
        print(switch[x], end=" ")


