import sys


def solution(unknown_array, known_array):
    answer = sorted(list(unknown_array & known_array))
    return len(answer), answer


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    unknown = {read().rstrip() for _ in range(N)}
    known = {read().rstrip() for _ in range(M)}
    count, names = solution(unknown, known)
    print(count)
    for name in names:
        print(name)
