import sys


def solution(n, m, array):
    d = [10001] * (m + 1) # 1원씩 있다해도 10000원 이상 만들수가 없음, 즉 경우의 수도 한정됨
    d[0] = 0
    for i in range(n):
        for j in range(array[i], m+1):  # 목표 m원
            d[j] = min(d[j], d[j-array[i]] + 1)
    return d[m]


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())     # n가지 화폐, m원 만들기
    bills = list(int(read()) for _ in range(N))
    ans = solution(N, M, bills)
    if ans == 10001:
        print(-1)
    else:
        print(ans)
