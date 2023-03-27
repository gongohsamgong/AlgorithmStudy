import sys


def solution(arr):
    target = 1
    for data in arr:
        if target < data:
            break
        target += data
    return target
        

if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    array = list(map(int, read().split()))
    array.sort()
    ans = solution(array)
    print(ans)
    