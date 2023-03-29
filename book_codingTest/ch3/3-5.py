import sys
from collections import Counter


def solution(n, m, arr):
    total = n * (n - 1) / 2
    counter_arr = Counter(arr)
    set_arr = list(set(arr))
    
    # for i in range(n):
    #
    # exception =
    
    # return total - exception


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())  # N: 볼링공의 개수, M: 공의 최대 무게
    array = list(map(int, read().split()))
    _list = Counter(array)
    print(_list[3])
    sset = set(array)
    print(list(sset)[0])
    # ans = solution(N, M, array)
    # print(ans)
