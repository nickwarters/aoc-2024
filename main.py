from typing import List
from functools import cache


@cache
def mix(secret: int, value: int) -> int: 
    result = secret ^ value 
    return result

@cache 
def prune(secret: int) -> int: 
    result = secret % 16777216
    return result

@cache
def evolve(secret: int, amt: int) -> int:
    for _ in range(amt):
        secret = prune(mix(secret, secret * 64))
        secret = mix(secret, int(secret / 32))
        secret = prune(mix(secret, secret * 2048))
    return secret



def solve_part_one(text: str) -> int: 

    result = 0
    steps = 2000
    init_secrets = list(map(int, text.splitlines()))

    result = sum([
        evolve(initial, steps) for initial in init_secrets
    ])


    return result


def solve_part_two(text: str) -> int: 
    result = 0



    return result


def main() -> int: 

    print('---- results ----')
    for part, func in (('one', solve_part_one), ('two', solve_part_two)):
        with open('input') as file: 
            text = file.read() 

        result = func(text)

        print(f'part {part}: {result}')

    return 0


if __name__ == '__main__': 
    raise SystemExit(main())

