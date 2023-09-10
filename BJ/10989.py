import sys


def solution(array):
    for num in range(10001):
        while array[num] != 0:
            print(num)
            array[num] -= 1


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    # for문 속에서 append 시 메모리 재할당으로 인해 메모리 초과가 나는 것이므로 배열로 대체
    numbers = [0] * 10001
    for i in range(N):
        numbers[int(read())] += 1
    solution(numbers)
