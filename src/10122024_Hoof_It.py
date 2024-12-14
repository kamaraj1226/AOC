# TAG: completed

import helper


def get_input(test):
    with open(helper.get_file_name(test), "r", encoding="utf-8") as f:
        return [list(map(int, line)) for line in f.read().splitlines()]


def part2(grid):
    row_max = len(grid)
    col_max = len(grid[0])

    def search(r, c):
        nonlocal row_max, col_max, grid

        is_valid = lambda x, y: x >= 0 and x < row_max and y >= 0 and y < col_max

        stack = [(0, (r, c))]
        count = 0

        while len(stack):
            val, (row, col) = stack.pop()

            if val == 9:
                count += 1
                continue
            _next = val + 1

            # check left
            if is_valid(row, col - 1) and _next == grid[row][col - 1]:
                stack.append((grid[row][col - 1], (row, col - 1)))

            # check right
            if is_valid(row, col + 1) and _next == grid[row][col + 1]:
                stack.append((grid[row][col + 1], (row, col + 1)))

            # check up
            if is_valid(row - 1, col) and _next == grid[row - 1][col]:
                stack.append((grid[row - 1][col], (row - 1, col)))

            # check down
            if is_valid(row + 1, col) and _next == grid[row + 1][col]:
                stack.append((grid[row + 1][col], (row + 1, col)))

        return count

    total = 0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col != 0:
                continue
            count = search(r, c)

            total += count
    print(f"{total}")


def part1(grid):
    row_max = len(grid)
    col_max = len(grid[0])

    def search(r, c):
        nonlocal row_max, col_max, grid

        is_valid = lambda x, y: x >= 0 and x < row_max and y >= 0 and y < col_max

        stack = [(0, (r, c))]
        count = 0
        visited = set()

        while len(stack):
            val, (row, col) = stack.pop()

            if val == 9:
                if (row, col) in visited:
                    continue
                visited.add((row, col))

                count += 1
                continue
            _next = val + 1

            # check left
            if is_valid(row, col - 1) and _next == grid[row][col - 1]:
                stack.append((grid[row][col - 1], (row, col - 1)))

            # check right
            if is_valid(row, col + 1) and _next == grid[row][col + 1]:
                stack.append((grid[row][col + 1], (row, col + 1)))

            # check up
            if is_valid(row - 1, col) and _next == grid[row - 1][col]:
                stack.append((grid[row - 1][col], (row - 1, col)))

            # check down
            if is_valid(row + 1, col) and _next == grid[row + 1][col]:
                stack.append((grid[row + 1][col], (row + 1, col)))

        return count

    total = 0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col != 0:
                continue
            count = search(r, c)
            # print(f"started searchin at {r,c} | {count}")
            total += count
    print(f"{total}")


def main():
    test = False
    inputs = get_input(test=test)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()
