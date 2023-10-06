def d(n):
    for num in str(n):
        n += int(num)
    return n


if __name__ == '__main__':
    numbers = set(range(1, 10001))  # 중복 없애기 위해 set 사용
    remove_list = []
    for n in numbers:
        remove_list.append(d(n))

    for remove_num in set(remove_list):
        numbers.discard(remove_num) # discard: 지우려는 요소가 없으면 빼고 지워, remove: 지우려는 요소가 없으면 오류 발생

    for self_num in numbers:
        print(self_num)