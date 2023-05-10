import sys


def binary_search(n, target, array):
    start, result = 0, 0
    end = max(array)
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in range(n):
            if array[i] > mid:
                total += array[i] - mid
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    ricecakes = list(map(int, read().split()))
    ans = binary_search(N, M, ricecakes)
    print(ans)
