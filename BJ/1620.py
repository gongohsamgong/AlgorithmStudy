import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    pokemons = {}
    for i in range(1, N+1):
        pokemon = read().rstrip()
        pokemons[pokemon] = i
        pokemons[i] = pokemon
    '''
    pokemons_index = {}
    index_pokemons = {}
    pokemons_index = {read().rstrip(): i+1 for i in range(N)}
    index_pokemons = {v: k for k, v in pokemons_index.items()}
    '''
    for _ in range(M):
        quiz = read().rstrip()
        if quiz.isdigit():
            print(pokemons.get(int(quiz)))
        else:
            print(pokemons.get(quiz))
