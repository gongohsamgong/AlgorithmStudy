import sys


def solution(n, l, start, end, location):
    cnt = 1
    for i in range(n):
        if start < location[i] < end:
            continue
        else:
            start = location[i] - 0.5
            end = start + l
            cnt += 1
    return cnt


if __name__ == '__main__':
    read = sys.stdin.readline
    N, L = map(int, read().split())
    location = list(map(int, read().split()))
    location.sort()
    start = location[0] - 0.5
    end = start + L
    ans = solution(N, L, start, end, location)
    print(ans)
    