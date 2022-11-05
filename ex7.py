import sys


def binary_search_rec(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_rec(array, target, start, mid-1)
    else:
        return binary_search_rec(array, target, mid+1, end)


def binary_search_rep(array, target, start, end):
    while start >= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == '__main__':
    read = sys.stdin.readline
    n, target = map(int, read().split())
    array = list(map(int, read().strip()))
    result1 = binary_search_rec(array, target, 0, n-1)
    result2 = binary_search_rep(array, target, 0, n-1)