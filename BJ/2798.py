import sys


"""
def solution(n, m, array):
    array.sort()
    candidate = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                candidate.append(array[i] + array[j] + array[k])
    candidate.sort()
    for num in candidate:
        if num > m:
            _index = candidate.index(num)
            result = max(candidate[0:_index])
            return result
    return max(candidate)
"""


"""
def solution(n, m, array):
    array.sort()
    result = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if array[i] + array[j] + array[k] > m:
                    continue
                else:
                    result = max(result, array[i] + array[j] + array[k])
    return result
"""


from itertools import combinations


def solution(n, m, array):
    nCr = combinations(array, 3)
    _max = 0
    for combination in nCr:
        _sum = sum(combination)
        if _sum > m:
            continue
        else:
            _max = max(_max, _sum)
    return _max


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    cards = list(map(int, read().split()))
    ans = solution(N, M, cards)
    print(ans)
