import sys


def solution(a, b):
    min_a = a.replace('6', '5')
    min_b = b.replace('6', '5')
    max_a = a.replace('5', '6')
    max_b = b.replace('5', '6')
    return int(min_a) + int(min_b), int(max_a) + int(max_b)


if __name__ == "__main__":
    read = sys.stdin.readline
    A, B = read().split()
    _min, _max = solution(A, B)
    print(_min, _max)
