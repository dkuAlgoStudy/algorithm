from collections import defaultdict


def solution(record):
    user = defaultdict(str)
    answer = []
    for i in record:
        state, uid = i.split(" ")[0], i.split(" ")[1]
        if state == "Enter" or state == "Change":
            user[uid] = i.split(" ")[2]
    for i in record:
        if i.split(" ")[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(user[i.split(" ")[1]]))
        elif i.split(" ")[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(user[i.split(" ")[1]]))

    return answer