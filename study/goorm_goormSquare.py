import sys


def solution(n, arr):
    count = 1
    arr.sort(key=lambda x: (x[1], x[0]))
    end_time = arr[0][1]
    for i in range(1, n):
        if arr[i][0] > end_time:
            count += 1
            end_time = arr[i][1]
    return count


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    timeline = [list(map(int, read().split())) for _ in range(N)]
    ans = solution(N, timeline)
    print(ans)
