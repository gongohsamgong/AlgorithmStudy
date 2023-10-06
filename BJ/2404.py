import sys
from fractions import Fraction


def back_tracking(num, _sum, multiple, path):
    if _sum == Fraction(p, q) and multiple <= a:
        global ans
        ans += 1
        return
    if len(path) == n:
        return
    for next_num in range(num, a//multiple + 1):
        if _sum + Fraction(1, next_num) <= Fraction(p, q) and multiple * next_num <= a:
            back_tracking(next_num, _sum + Fraction(1, next_num), multiple * next_num, path + [next_num])


if __name__ == "__main__":
    read = sys.stdin.readline
    p, q, a, n = map(int, read().split())


