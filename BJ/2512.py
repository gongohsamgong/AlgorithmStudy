import sys

def solution(m, arr):
    start = 0
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2
        _sum = 0
        for val in arr:
            if val <= mid:
                _sum += val
            else:
                _sum += mid
        if _sum <= m:
            start = mid + 1
        else:
            end = mid - 1
    return end  # 왜 mid가 아닌가?


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    arr = list(map(int, read().split()))
    m = int(read())
    ans = solution(m, arr)
    print(ans)
