import sys


def solution(m, k, arr):
    _sum = 0
    cnt = 0
    arr.sort(reverse=True)
    first = arr[0]
    second = arr[1]
    for i in range(m):
        if cnt == k:
            _sum += second
            cnt = 0
            continue
        _sum += first
        cnt += 1
    return _sum


if __name__ =='__main__':
    read = sys.stdin.readline
    N, M, K = map(int, read().split())
    array = list(map(int, read().split()))
    answer = solution(M, K, array)
    print(answer)
