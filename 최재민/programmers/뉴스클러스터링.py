from collections import defaultdict
import math


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    news1, news2 = defaultdict(int), defaultdict(int)

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            news1[str1[i:i + 2]] += 1

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            news2[str2[i:i + 2]] += 1

    inter = 0
    for key1, value1 in news1.items():
        for key2, value2 in news2.items():
            if key1 == key2:
                inter += min(value1, value2)

    uni = sum(news1.values()) + sum(news2.values()) - inter

    if uni == 0 and inter == 0:
        answer = 65536
    else:
        answer = (inter / uni) * 65536

    return math.floor(answer)
