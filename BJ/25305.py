import sys


def solution(k, array):
    array.sort(reverse=True)
    cut_line = array[k-1]
    return cut_line


if __name__ == "__main__":
    read = sys.stdin.readline
    N, k = map(int, read().split())
    scores = list(map(int, read().split()))
    answer = solution(k, scores)
    print(answer)
