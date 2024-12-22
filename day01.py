from collections import Counter


def solve_part_one(text: str) -> int: 

    result = 0

    lines = text.splitlines() 
    left = [int(x[:5]) for x in lines]
    right = [int(x[-5:]) for x in lines]

    left.sort() 
    right.sort() 

    diffs = []

    for l, r in zip(left, right): 
        d = max(l, r) - min(l, r) 
        diffs.append(d)

    result = sum(diffs)


    return result


def solve_part_two(text: str) -> int: 
    result = 0

    lines = text.splitlines() 
    left = [x[:5] for x in lines]
    right = [x[-5:] for x in lines]
    counts = Counter(right)

    totals = [int(x) * counts.get(x, 0) for x in left]

    result = sum(totals)



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

