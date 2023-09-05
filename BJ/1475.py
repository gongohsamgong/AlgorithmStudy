import sys
import math
from collections import Counter


def solution(number):
    number = number.replace('9', '6')
    count_num = Counter(number)
    count_num['6'] = math.ceil(count_num['6'] / 2)
    common = count_num.most_common()
    return common[0][1]


if __name__ == '__main__':
    read = sys.stdin.readline
    N = read().rstrip()
    ans = solution(N)
    print(ans)
