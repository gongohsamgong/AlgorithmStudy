import sys
import itertools


if __name__ == "__main__":
    read = sys.stdin.readline
    N, S = map(int, read().split())
    array = list(map(int, read().split()))
    nCr = []
    cnt = 0
    for i in range(1, N+1):
        nCr.append(list(itertools.combinations(array, i)))
    for arr in nCr:
        for comb in arr:
            if sum(comb) == S:
                cnt += 1
    print(cnt)
