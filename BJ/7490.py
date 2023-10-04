import copy
import sys


def recur(arr, n):
    if len(arr) == n:
        global operators
        operators.append(copy.deepcopy(arr))
        return
    arr.append(' ')
    recur(arr, n)
    arr.pop()

    arr.append('+')
    recur(arr, n)
    arr.pop()

    arr.append('-')
    recur(arr, n)
    arr.pop()


if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        N = int(read())
        operators = []
        recur([], N-1)
        for operator in operators:
            statement = ''
            for i in range(N-1):
                statement += str(i+1) + operator[i]
            statement += str(N)
            if eval(statement.replace(' ', '')) == 0:
                print(statement)
        print()
