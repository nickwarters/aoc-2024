
def solve_part_one(text: str) -> int: 

    result = 0

    lines = [list(map(int, x.split(' '))) for x in text.splitlines()]

    for line in lines: 
        if len(set(line)) != len(line): 
            continue 

        safe = True 
        prev = None
        for i in range(len(line) - 1): 
            if abs(line[i] - line[i + 1]) > 3: 
                safe = False 
                break

            if prev is not None: 
                if line[i] > line[i + 1] and prev < line[i]: 
                    safe = False 
                    break 
                if line[i] < line[i + 1] and prev > line[i]: 
                    safe = False 
                    break

            prev = line[i]

        result += int(safe)


    return result


def solve_part_two(text: str) -> int: 
    result = 0

    lines = [list(map(int, x.split(' '))) for x in text.splitlines()]

    for line in lines: 
        prev = 0
        bad = 0
        last_safe = 0
        for i in range(1, len(line)):
            safe = True
            diff = abs(line[i] - line[last_safe])
            if diff > 3 or diff == 0: 
                safe = False
                
            prev = line[max(last_safe - 1, 0)]
            if line[i] > line[last_safe] and prev < line[last_safe]: 
                safe = False
            if line[i] < line[last_safe] and prev > line[last_safe]: 
                safe = False

            if safe: 
                last_safe = i
            else: 
                bad += 1
        print(f'{line=}, {bad=}')
        result += int(bad < 2)



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

