def solution(box):
    # Write your code here
    max_val = box[0]
    avg_bread = sum(box) / len(box)
    if avg_bread - int(avg_bread) >= 0.5:
        avg_bread = int(avg_bread) + 1
    else:
        avg_bread = int(avg_bread)
    print('avg_bread = ', avg_bread)
    max_index = box.index(max(box))
    if max_index == 0:
        return max_val
    print(box)
    while True:
        current_max_index = box.index(max(box))
        print('current_max_index =', current_max_index)
        # select k
        if sum(map(lambda x: 0 if x == avg_bread else 1, box)) > 2:
            partial_sum = sum(box[0:current_max_index])
            k = avg_bread - partial_sum % avg_bread
        else:
            k = box[current_max_index] - avg_bread
            box[current_max_index] -= k
            box[current_max_index - 1] += k
            return max(box)
        print('k =', k)
        box[current_max_index] -= k
        box[current_max_index - 1] += k
        print(box)
    return max(box)