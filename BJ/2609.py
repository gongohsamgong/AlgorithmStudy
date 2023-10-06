import sys
import math


if __name__ == "__main__":
    read = sys.stdin.readline
    a, b = map(int, read().split())
    print(math.gcd(a, b))
    print(math.lcm(a, b))
