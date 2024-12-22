from typing import List


def solve_part_one(text: str) -> int: 

    result = 0

    m = text.splitlines()
    start_pos = (0, 0) 
    for r, row in enumerate(m): 
        if '^' not in row: 
            continue 

        c = row.index('^')

        start_pos = (r, c) 

    current_pos = start_pos
    current_dir = (-1, 0)
    visited = set() 

    while True: 
        next_pos = current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]
        visited.add(current_pos)
        if next_pos[0] < 0 or next_pos[0] == len(m): 
            break 
        if next_pos[1] < 0 or next_pos[1] == len(m[0]): 
            break


        new_dir = current_dir

        if m[next_pos[0]][next_pos[1]] == '#': 
            if current_dir[0] == -1: 
                new_dir = (0, 1)
            elif current_dir[0] == 1: 
                new_dir = (0, -1)
            elif current_dir[1] == -1: 
                new_dir = (-1, 0)
            else: 
                new_dir = (1, 0)

            current_dir = new_dir

            continue 

        current_pos = next_pos

    result = len(visited)

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

