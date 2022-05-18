import sys

sound = sys.stdin.readline().rstrip()
cnt = 0
min_num = 0

howl = {'q': 0, 'u': 0, 'a': 0, 'c': 0, 'k': 0}

for i in sound:

    if i == 'q':
        howl[i] += 1
        cnt += 1
        if cnt > min_num:
            min_num = cnt

    elif i == 'u':
        howl[i] += 1
        if howl['q'] < howl['u']:
            min_num = -1
            break

    elif i == 'a':
        howl[i] += 1
        if howl['u'] < howl['a']:
            min_num = -1
            break

    elif i == 'c':
        howl[i] += 1
        if howl['a'] < howl['c']:
            min_num = -1
            break

    elif i == 'k':
        howl[i] += 1
        cnt -= 1
        if howl['c'] < howl['k']:
            min_num = -1
            break


if len(sound) % 5 != 0:
    min_num = -1
for i in howl:
    if howl[i] != howl['q']:
        min_num = -1

print(min_num)
