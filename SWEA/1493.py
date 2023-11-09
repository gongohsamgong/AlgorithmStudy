#import sys
#sys.stdin = open("input.txt", "r")

def two_to_one(x, y):
    criterion = x + y
    start = 1 + (criterion - 2) * (criterion - 1) // 2
    for i in range(x - 1):
        start += 1
    return start


def one_to_two(p):
    start, i = 1, 1
    while True:
        start += i
        if start > p:
            start -= i
            break
        i += 1
    criterion = 2
    while True:
        if start == 1 + (criterion - 2) * (criterion - 1) // 2:
            break
        criterion += 1
    x, y = 1, criterion - 1
    for i in range(p - start):
        x += 1
        y -= 1
    return x, y


T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    x1, y1 = one_to_two(p)
    x2, y2 = one_to_two(q)
    print("#%d %d" % (test_case, two_to_one(x1+x2, y1+y2)))
