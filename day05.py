from typing import List

def is_valid(run: List[int], rules: List[List[int]]) -> bool: 

    for l, r in rules: 
        if l not in run or r not in run: 
            continue 

        if run.index(l) > run.index(r): 
            return False 

    return True


def fixup(run: List[int], rules:List[List[int]]) -> List[int]: 
    while not is_valid(run, rules): 
        for l, r in rules: 
            if l not in run or r not in run: 
                continue 

            li, ri = run.index(l), run.index(r)
            
            if li < ri: 
                continue 

            run[li] = r 
            run[ri] = l 
            break


    return run


def solve_part_one(text: str) -> int: 

    result = 0

    rules, runs = text.split('\n\n')

    rules = [list(map(int, x.split('|'))) for x in rules.splitlines()]
    runs = [list(map(int, x.split(','))) for x in runs.splitlines()]

    for run in runs: 
        if not is_valid(run, rules): 
            continue

        assert len(run) % 2 != 0

        result += run[int(len(run) / 2)]

    return result


def solve_part_two(text: str) -> int: 
    result = 0

    rules, runs = text.split('\n\n')

    rules = [list(map(int, x.split('|'))) for x in rules.splitlines()]
    runs = [list(map(int, x.split(','))) for x in runs.splitlines()]

    for run in runs: 
        if is_valid(run, rules): 
            continue

        run = fixup(run, rules)

        result += run[int(len(run) / 2)]


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

