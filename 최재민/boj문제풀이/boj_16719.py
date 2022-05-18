ZOAC = list(input())

answer = [""] * len(ZOAC)

def sorting(start, ZOAC):
    if not ZOAC:
        return
    min_val = min(ZOAC)
    temp = ZOAC.index(min_val)

    answer[start + temp] = min_val
    print("".join(answer))
    sorting(start + temp + 1, ZOAC[temp+1:])
    sorting(start,ZOAC[:temp])


sorting(0, ZOAC)