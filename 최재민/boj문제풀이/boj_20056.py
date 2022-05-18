from copy import deepcopy
import sys

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int,sys.stdin.readline().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    board[r-1][c-1].append([m, s, d])

for _ in range(K):
    m_board = [[[]for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] != []:
                for k in range(len(board[i][j])):
                    moved_m,moved_s,moved_d = board[i][j][k]
                    nx = i + dx[moved_d] * moved_s
                    ny = j + dy[moved_d] * moved_s
                    nx = (nx + N) % N
                    ny = (ny + N) % N
                    m_board[nx][ny].append([moved_m,moved_s,moved_d])

    for i in range(N):
        for j in range(N):
            if len(m_board[i][j]) > 1:
                sm, ss, sd = 0, 0, []
                cnt = len(m_board[i][j])
                for k in range(cnt):
                    sm += m_board[i][j][k][0]
                    ss += m_board[i][j][k][1]
                    sd.append(m_board[i][j][k][2] % 2)

                sm = int(sm/5)
                ss = int(ss/cnt)
                m_board[i][j] = []

                if sm != 0:
                    if sum(sd)==0 or sum(sd) == cnt:
                        for x in range(4):
                            m_board[i][j].append([sm, ss, x * 2])
                    else:
                        for y in range(4):
                            m_board[i][j].append([sm,ss,y*2 + 1])
    board = deepcopy(m_board)

answer = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != []:
            for k in range(len(board[i][j])):
                answer += board[i][j][k][0]

print(answer)