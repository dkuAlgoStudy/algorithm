import sys
from collections import defaultdict
from datetime import datetime


def strTotime(s):
    d, time = s.split('/')
    d = int(d)
    h, m = map(int, time.split(':'))
    total = m + h * 60 + d * 24 * 60
    return total


N, L, F = list(input().split())
N = int(N)
F = int(F)
L = strTotime(L)
borrow_dict = defaultdict(dict)
fee_dict = defaultdict(int)



for i in range(N):
    borrow = sys.stdin.readline()
    date = borrow[:16]
    time = datetime.strptime(date, '%Y-%m-%d %H:%M')
    part, name = borrow[16:].split()
    if borrow_dict[name].get(part):
        borrowed_time = time - borrow_dict[name][part]
        day = borrowed_time.days
        min = borrowed_time.seconds // 60
        to_time = day * 60 * 24 + min
        if to_time > L:
            fee_dict[name] += (to_time - L) * F
        del borrow_dict[name][part]
    else:
        borrow_dict[name][part] = time

if len(fee_dict.keys()):
    key_list = sorted(fee_dict.keys())

    for key in key_list:
        print(key, int(fee_dict[key]))

else:
    print(-1)

