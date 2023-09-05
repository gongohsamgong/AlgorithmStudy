import sys


def solution(people):
    for i in people:
        rank = 1
        for j in people:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        print(rank, end=' ')


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    people = [list(map(int, read().split())) for _ in range(N)]
    solution(people)
