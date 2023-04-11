import sys


def solution(n):
    cnt = 0
    start = 665
    # flag = True
    while True:
        start += 1
        if '666' in str(start):
            cnt += 1
        if cnt == n:
            break
    return start


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    ans = solution(N)
    print(ans)
