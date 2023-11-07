# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque

for _ in range(10):
    test_case = int(input())
    password = deque(list(map(int, input().split())))
    while 0 not in password:
        for i in range(1, 6):
            password[0] -= i
            password.append(password.popleft())
            if password[-1] <= 0:
                password[-1] = 0
                break
    print('#{}'.format(test_case), *password)
