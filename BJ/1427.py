import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    # numbers = sorted(list(map(int, read().rstrip())), reverse=True)
    numbers = list(map(int, read().rstrip()))
    numbers.sort(reverse=True)
    for i in range(len(numbers)):
        print(numbers[i], end='')
