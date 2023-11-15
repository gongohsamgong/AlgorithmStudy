from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    schedule = deque(list(map(int, input().split())))
    answer = int(1e9)
    class_per_week = sum(schedule)
    for i in range(7):
        schedule.append(schedule.popleft())
        class_days, actual_days = 0, 0
        cycle = 0
        while True:
            if class_days >= n:
                class_days -= class_per_week
                cycle -= 1
                break
            class_days += class_per_week
            cycle += 1
        actual_days += 7 * cycle
        if class_days < n:
            for j in range(7):
                if class_days == n:
                    break
                class_days += schedule[j]
                actual_days += 1
        answer = min(answer, actual_days)
    print("#%d %d" % (test_case, answer))
