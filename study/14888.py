import sys

# 매개변수로 depth(개수), val(값), 그리고 =, -, *, //의 개수를 차례로 입력받음
def dfs(depth, val, plus, minus, multiply, divide):
    # 재귀함수를 사용하기 때문에 global 변수로 선언해야 값이 초기화되지 않음
    global maximum, minimum
    # 주어진 n개의 수열에 대해 dfs를 거쳤다면 최대, 최소값을 산출
    if depth == n:
        maximum = max(val, maximum)
        minimum = min(val, minimum)
        return maximum, minimum

    # 산술 연산자에 따라, depth는 하나 늘어나고 val에 해당 연산자로 계산을 하고, 해당 연산자는 사용되었으므로 개수를 하나 줄임
    if plus:
        dfs(depth + 1, val + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, val - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, val * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(val / num[depth]), plus, minus, multiply, divide - 1)


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    num = list(map(int, read().split()))    # 숫자를 배열로 입력받음
    op = list(map(int, read().split()))     # +, -, *, // 순으로 연산자의 개수를 배열로 입력받음
    maximum = -1e9
    minimum = 1e9
    dfs(1, num[0], op[0], op[1], op[2], op[3])
    print(maximum)
    print(minimum)





