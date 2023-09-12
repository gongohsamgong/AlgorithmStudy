import sys


def solution(array):
    length = len(array)
    total = set()
    for i in range(length):
        for j in range(i, length):
            total.add(array[i:j+1])
    return len(total)


if __name__ == "__main__":
    read = sys.stdin.readline
    str_array = read().rstrip()
    answer = solution(str_array)
    print(answer)
