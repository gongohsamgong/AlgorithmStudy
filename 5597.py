import sys


def find(arr):
    result = []
    for i in range(1, 31):
        if i not in arr:
            result.append(i)
    return result


if __name__ == '__main__':
    read = sys.stdin.readline
    array = []
    for i in range(28):
        array.append(int(read()))
    res = find(array)
    for i in range(2):
        print(res[i])