def solve_part_one(text: str) -> int: 

    result = 0

    lines = text.splitlines() 

    seen = set()

    r = c = 0

    valid = ('XMAS', 'SAMX')

    while r < len(lines) - 3: 
        c = 0
        while c < len(lines[0]) - 3:
            for points in (
                ((r, c), (r,c + 1), (r,c + 2), (r,c + 3)), 
                ((r + 1,c), (r + 1,c + 1), (r + 1,c + 2), (r + 1,c + 3)), 
                ((r + 2,c), (r + 2,c + 1), (r + 2,c + 2), (r + 2,c + 3)), 
                ((r + 3,c), (r + 3,c + 1), (r + 3,c + 2), (r + 3,c + 3)), 
                
                ((r,c), (r + 1,c), (r + 2,c), (r + 3,c)), 
                ((r,c + 1), (r + 1,c + 1), (r + 2,c + 1), (r + 3,c + 1)), 
                ((r,c + 2), (r + 1,c + 2), (r + 2,c + 2), (r + 3,c + 2)), 
                ((r,c + 3), (r + 1,c + 3), (r + 2,c + 3), (r + 3,c + 3)), 
                
                ((r,c), (r + 1,c + 1), (r + 2,c + 2), (r + 3,c + 3)), 
                ((r,c + 3), (r + 1,c + 2), (r + 2,c + 1), (r + 3,c)), 
            ):
                if points in seen:
                    continue 

                seen.add(points)

                value = ''.join([
                    lines[points[0][0]][points[0][1]],
                    lines[points[1][0]][points[1][1]],
                    lines[points[2][0]][points[2][1]],
                    lines[points[3][0]][points[3][1]],
                ])


                if value in valid: 
                    result += 1

            c += 1
        r += 1

    return result


def solve_part_two(text: str) -> int: 
    result = 0

    lines = text.splitlines() 

    seen = set()

    r = c = 0

    valid = ('MSAMS', 'MMASS', 'SMASM', 'SSAMM')

    while r < len(lines) - 2: 
        c = 0
        while c < len(lines[0]) - 2:
            for points in (
                ((r, c), (r,c + 2), (r + 2, c + 1), (r + 2, c), (r + 2, c + 2)), 
            ):
                if points in seen:
                    continue 

                seen.add(points)

                value = ''.join([
                    lines[points[0][0]][points[0][1]],
                    lines[points[1][0]][points[1][1]],
                    lines[points[2][0]][points[2][1]],
                    lines[points[3][0]][points[3][1]],
                    lines[points[4][0]][points[4][1]],
                ])


                if value in valid: 
                    result += 1

                print(f'{points=}, {value=}, {result=}')

            c += 1
        r += 1


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

