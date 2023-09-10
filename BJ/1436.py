import sys


def solution(n):
    number, cnt = 0, 0
    while True:
        number += 1
        if '666' in str(number):
            cnt += 1
            if cnt == n:
                return number


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    answer = solution(N)
    print(answer)
