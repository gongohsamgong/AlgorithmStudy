class Checker:
    def __init__(self, func):
        print("Checker.__init__ called")
        self.func = func

    def __call__(self, *args):
        print("Checker.__call__ called")
        if len(args) > 0 and args[0] >= 1:
            return self.func(args[0])
        else:
            raise Exception("n(%d)은 1보다 크거나 같은 정수여야 합을 구할 수 있음" % args[0])

@Checker
def get_sum(n):
    sum_ = 0
    for i in range(1, n+1):
        sum_ += i
    return sum_

if __name__ == '__main__':
    try:
        print("%d" % get_sum(10))
        print("%d" % get_sum(-1))
    except Exception as ex:
        print("예외: " + str(ex))