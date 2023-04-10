import sys

def solution(n):
    cnt = 0
    start = 665
    while True:
        start += 1
        if '666' in str(start) and cnt == n:
            cnt += 1
        return start


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    ans = solution(N)
    print(ans)
