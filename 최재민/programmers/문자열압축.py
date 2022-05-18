def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        st = ''
        cnt = 1
        temp = s[:i]

        for j in range(i, len(s), i):
            if temp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    st += str(cnt) + temp
                else:
                    st += temp
                temp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            st += str(cnt) + temp
        else:
            st += temp

        result.append(len(st))

    return min(result)
