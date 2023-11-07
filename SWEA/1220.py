import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    n = int(input())
    # 1:N, 2:S, N극:위, S극:아래
    table = [list(map(int, input().split())) for _ in range(100)]
    answer = 0

    for j in range(100):
        check = []
        flag_1 = False
        for i in range(100):
            if table[i][j] == 1:
                flag_1 = True
            if flag_1 and table[i][j] == 2:
                check.append((i, j))
                flag_1 = False
        if check:
            answer += len(check)

    print("#%d %d" % (test_case, answer))
