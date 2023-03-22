import sys


def solution(s):
    temp = 0
    length = len(s)
    for i in range(length):
        if i == length - 1:
            return temp
        if s[i] <= 1:
            temp = s[i] + s[i+1]
            s[i+1] = temp
        else:
            temp = s[i] * s[i+1]
            s[i+1] = temp


if __name__ == '__main__':
    read = sys.stdin.readline
    S = list(read().rstrip())
    S_int = [int(num) for num in S]
    # print(S_int)
    ans = solution(S_int)
    print(ans)
    