def solution(lines):
    answer = 0
    start = []
    end = []
    for i in lines:
        time = i.split(" ")
        start.append(get_start_time(time[1], time[2]))
        end.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt = 0
        current_end = end[i]
        for j in range(i, len(lines)):
            if current_end > start[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer


def get_time(time):
    return (int(time[:2])*3600 + int(time[3:5])*60 + int(time[6:8])) * 1000 + int(time[9:])


def get_start_time(time, duration_time):
    return get_time(time) - int(float(duration_time[:-1])*1000) + 1