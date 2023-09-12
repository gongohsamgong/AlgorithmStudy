import sys


def solution(a, b):
    set_a, set_b = set(a), set(b)
    return len(set_a - set_b) + len(set_b - set_a)


if __name__ == "__main__":
    read = sys.stdin.readline
    len_A, len_B = map(int, read().split())
    A = list(map(int, read().split()))
    B = list(map(int, read().split()))
    answer = solution(A, B)
    print(answer)
