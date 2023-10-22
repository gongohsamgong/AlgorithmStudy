def solution(nums):
    set_pokemons = set(nums)
    answer = len(nums) // 2
    while answer > len(set_pokemons):
        answer -= 1
    return answer
