import re


def solve_part_one(text: str) -> int: 

    result = 0

    mults = re.findall(r'mul\((\d+),(\d+)\)', text)

    for a, b in mults: 
        result += int(a) * int(b)

    return result


def solve_part_two(text: str) -> int: 
    result = 0

    all_mults = re.findall(r'(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))', text)

    active = True 

    for m, y, n in all_mults: 
        if n: 
            active = False 
            continue 

        if y: 
            active = True 
            continue 

        if not active: 
            continue 

        a, b = m.split(',')

        result += int(a.removeprefix("mul(")) * int(b.removesuffix(')'))

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

