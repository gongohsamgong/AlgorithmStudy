import sys


def solution(n):
    result = 0
    if n == 1:
        least, most = 1, 9
    else:
        least, most = 2, 0
        for i in range(n-1):
            least += 9 * 10 ** i
        for j in range(n):
            most += 9 * 10 ** j
    for num in range(least, most + 1):
        result = result + 1 % 987654321
        str_num = str(num)
        for digit in range(n-1):
            if '0' in str_num or abs(int(str_num[digit]) - int(str_num[digit + 1])) > 2:
                result -= 1
                break
    return result


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    answer = solution(n)
    print(answer)
