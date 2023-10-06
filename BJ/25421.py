import sys


def solution(n):
    num = [1 for _ in range(9)]
    while n != 1:
        temp = []
        for i in range(9):
            # 1X: 3, 2X: 4, 3X: 5, 4X: 5, ..., 9X: 3
            temp.append(sum(num[max(0, i-2): min(10, i+3)]) % 987654321)
        num = temp
        n -= 1
    return sum(num) % 987654321


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    answer = solution(n)
    print(answer)
