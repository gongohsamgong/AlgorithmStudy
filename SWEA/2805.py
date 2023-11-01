T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().rstrip())) for _ in range(N)]
    harvest, start, end = 0, N // 2, N // 2
    for i in range(N):
        for j in range(start, end + 1):
            harvest += farm[i][j]
        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print("#%d %d" % (test_case, harvest))
