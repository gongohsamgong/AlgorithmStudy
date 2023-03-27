import sys


def solution(array):
    group = 0
    for i in range(len(array)):
        if i == len(array) - 1:
            return group // 2
        if array[i] != array[i+1]:
            group += 1


if __name__ == '__main__':
    read = sys.stdin.readline
    S = read()
    ans = solution(S)
    print(ans)
    