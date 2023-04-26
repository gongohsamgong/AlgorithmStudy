import sys


def solution(n, arr):
    count = []
    arr.sort(key=lambda x: x[0])

    return max(count)


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    timeline = [list(map(int, read().split())) for _ in range(N)]
    # print(timeline)
    ans = solution(N, timeline)
    print(ans)
