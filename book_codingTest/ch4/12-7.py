import sys


def solution(n):
    length = len(n)
    int_n = [int(num) for num in n]
    sum1 = sum(int_n[:length//2])
    sum2 = sum(int_n[length//2:])
    if sum1 == sum2:
        return 'LUCKY'
    else:
        return 'READY'


if __name__ == '__main__':
    read = sys.stdin.readline
    N = read().rstrip()
    ans = solution(N)
    print(ans)
