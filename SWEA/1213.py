import sys
sys.stdin = open("test_input.txt", "r")

"""
for _ in range(10):
    answer = 0
    test_case = int(input())
    find = input()
    given_string = input()
    for i in range(len(given_string) - len(find) + 1):
        if find == given_string[i:i+len(find)]:
            answer += 1
    print("#%d %d" % (test_case, answer))

"""

for _ in range(10):
    test_case = int(input())
    find = input()
    given_string = input()
    answer = given_string.count(find)
    print("#%d %d" % (test_case, answer))
