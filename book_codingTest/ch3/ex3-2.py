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


"""
import sys


def solution(n, m, k, array):
    array.sort(reverse=True)
    first_max = array[0]
    second_max = array[1]
    _sum, count = 0, 0
    for i in range(m):
        if count == k:
            _sum += second_max
            count = 0
        else:
            _sum += first_max
            count += 1
    return _sum


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M, K = map(int, read().split())
    numbers = list(map(int, read().split()))
    ans = solution(N, M, K, numbers)
    print(ans)

"""