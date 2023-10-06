import sys


def solution(k, arr):
    index = 0
    while True:
        if arr[index] == 0:
            arr.pop(index)
            arr.pop(index-1)
            index -= 1
        else:
            index += 1
        if index == len(arr):
            return sum(arr)


if __name__ == "__main__":
    read = sys.stdin.readline
    K = int(read())
    money = [int(read()) for _ in range(K)]
    ans = solution(K, money)
    print(ans)
