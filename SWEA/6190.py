# import sys
# sys.stdin = open("s_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    numbers = set()
    answer = -1
    for i in range(N-1):
        for j in range(i+1, N):
            multiply = A[i] * A[j]
            str_multiply = str(multiply)
            flag = True
            for k in range(len(str_multiply) - 1):
                if int(str_multiply[k]) > int(str_multiply[k+1]):
                    flag = False
            if flag:
                answer = max(answer, multiply)
    print("#%d %d" % (test_case, answer))
