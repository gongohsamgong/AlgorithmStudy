import sys


def solution(sorted_arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if sorted_arr[mid] == target:
            return 'yes'
        elif sorted_arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 'no'


if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    array = list(map(int, read().split()))
    array.sort()
    M = int(read())
    find = list(map(int, read().split()))
    for i in range(M):
        ans = solution(array, find[i], 0, N-1)
        print(ans, end=' ')



'''
read = sys.stdin.readline
N = int(read())
array = list(map(int, read().split()))
M = int(read())
find = list(map(int, read().split()))

for i in range(M):
    if find[i] in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''