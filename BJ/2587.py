import sys


def solution(array):
    avg = sum(array) / 5
    array.sort()
    med = array[2]
    return avg, med


if __name__ == "__main__":
    read = sys.stdin.readline
    numbers = [0] * 5
    for i in range(5):
        numbers[i] = int(read())
    average, median = solution(numbers)
    print("%d\n%d" %(average, median))
