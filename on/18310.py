import sys


def calculate(num, array):
    sum_array = []
    for i in range(num):
        sum_ = 0
        for j in range(num):
            sum_ += abs(array[i] - array[j])
        sum_array.append(sum_)
    id_ = sum_array.index(min(sum_array))
    return array[id_]


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    arr = list(map(int, read().split()))
    print(calculate(n, arr))