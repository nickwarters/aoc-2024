from typing import List, Tuple, Set

Point = Tuple[int, int]

def get_possible_paths(grid: List[List[str]], current: Point, seen: Set[Point]) -> List[Point]: 
    possible_paths: List[Point] = []

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_pos = (current[0] + dx, current[1] + dy)
        if (new_pos[0] < 0) or new_pos[0] == len(grid): 
            continue 

        if (new_pos[1] < 0) or new_pos[1] == len(grid[0]): 
            continue

        if new_pos in  seen: 
            continue 
        
        if grid[new_pos[0]][new_pos[1]] == '#': 
            continue 


        possible_paths.append(new_pos)


    return possible_paths



def solve_part_one(text: str) -> int: 

    result = 0

    coords = set([tuple(map(int, line.split(','))) for line in text.splitlines()[:1024]])

    grid = [['.' for _ in range(71)] for _ in range(71)]

    for x, y in coords: 
        grid[y][x] = '#'

    current_pos = (0, 0)
    dest = (70, 70)
    prev = current_pos

    seen: Set[Point] = {(0, 0)}
    queue: List[Tuple[Point, int]] = [(current_pos, 0)]

    while queue: 
        current_pos, current_cost = queue.pop(0)

        if current_pos == dest: 
            result = current_cost
            break

        for p in get_possible_paths(grid, current_pos, seen): 
            queue.append((p, current_cost + 1))
    
            seen.add(p)
        


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

