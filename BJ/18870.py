import sys


def solution(n, array):
    new_array = list(set(array))
    new_array.sort()
    # numdict = {}
    # for i in range(len(new_array)):
    #     numdict[new_array[i]] = i
    num_dict = {new_array[i]: i for i in range(len(new_array))}
    for i in range(n):
        print(num_dict[array[i]], end=' ')


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    numbers = list(map(int, read().split()))
    solution(N, numbers)
