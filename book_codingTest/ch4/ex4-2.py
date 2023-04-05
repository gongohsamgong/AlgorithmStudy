import sys


def solution(n):
    cnt = 0
    for i in range(n + 1):  # 시
        for j in range(60):  # 분
            for k in range(60):  # 초
                string = str(i) + str(j) + str(k)
                if '3' in string:
                    cnt += 1
    return cnt


if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    ans = solution(N)
    print(ans)
    