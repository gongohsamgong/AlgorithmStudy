import sys


def solution(s):
    length = len(s)
    for i in range(length):
        if i == length - 1:
            return s[i]
        if s[i] <= 1:
            s[i+1] += s[i]
        else:
            s[i+1] *= s[i]


if __name__ == '__main__':
    read = sys.stdin.readline
    S = list(read().rstrip())
    S_int = [int(num) for num in S]
    ans = solution(S_int)
    print(ans)
    