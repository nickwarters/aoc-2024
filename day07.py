from typing import List
from itertools import permutations


def solve_part_one(text: str) -> int: 

    result = 0

    lines = text.splitlines() 
    for line in lines: 
        parts = line.split(': ')
        target = int(parts[0])
        nums = list(map(int, parts[1].split()))
        print(f'running {line=}')

        for p in permutations('*+' * len(nums), len(nums) - 1):
 
            r = nums[0]

            for i in range(1, len(nums)): 
                if p[i - 1] == '+': 
                    r += nums[i]
                else: 
                    r *= nums[i]

            if r == target: 
                result += target 
                break

        


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

