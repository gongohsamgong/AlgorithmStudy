import sys


def cut(array, start, end, m):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for x in array:
            if x > mid:
                total += x - mid
            else:
                continue
        if total < m:
            end = mid - 1
        else:
            start = mid + 1
    return end  # 왜 mid가 아니라 end인가..... m 이상이니까 최대한 큰 거니까... 인듯...? 응 맞는듯


if __name__ == '__main__':
    read = sys.stdin.readline
    n, m = map(int, read().split())
    arr = list(map(int, read().split()))
    print(cut(arr, 0, max(arr), m))
