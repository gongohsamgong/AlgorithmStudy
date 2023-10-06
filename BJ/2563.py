import sys


def solution(paper_location):
    total = 0
    array = [[0] * 100 for _ in range(100)]
    for loc in paper_location:
        for i in range(loc[1], loc[1] + 10):
            for j in range(loc[0], loc[0] + 10):
                array[i][j] = 1
    for k in range(100):
        total += array[k].count(1)
    return total


if __name__ == "__main__":
    read = sys.stdin.readline
    paper_number = int(read())
    paper_locations = []
    for _ in range(paper_number):
        paper_locations.append(list(map(int, read().split())))
    answer = solution(paper_locations)
    print(answer)
