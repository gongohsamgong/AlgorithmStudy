import copy
import sys
from itertools import product


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


def product_solution(n):
    result = []
    for insert in product(['+', '-', ' '], repeat=n-1):
        num = 1
        expression = ''
        for sign in insert:
            expression += str(num) + sign
            num += 1
        expression += str(n)

        if eval(expression.replace(' ', '')) == 0:
            result.append(expression)

    return sorted(result)


if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        N = int(read())
        '''        
        operators = []
        recur([], N-1)
        for operator in operators:
            statement = ''
            for i in range(N-1):
                statement += str(i+1) + operator[i]
            statement += str(N)
            if eval(statement.replace(' ', '')) == 0:
                print(statement)
        '''
        answer_arrays = product_solution(N)
        for answer in answer_arrays:
            print(answer)
        print()
