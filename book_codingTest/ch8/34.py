import sys


"""
def solution(n, array):
    cnt = 0
    for i in range(n-1):
        if array[i] < array[i+1]:
            cnt += 1
        else:
            continue
    return cnt
"""


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    power = list(map(int, read().split()))
    ans = solution(N, power)
    print(ans)
