import sys


def solution(m, arr):
    start = 0
    end = max(arr)
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in arr:
            if x > mid:
                total += x-mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    ricecake = list(map(int, read().split()))
    ans = solution(M, ricecake)
    print(ans)
