# TAG: completed

import helper


def get_input(test):
    with open(helper.get_file_name(test), "r", encoding="utf-8") as f:
        return list(map(int, f.read().split()))


def part2(pebbles):
    cache = {}

    def count(stone, steps):
        if (stone, steps) in cache:
            return cache[(stone, steps)]

        if steps == 0:
            return 1

        if stone == 0:
            val = count(1, steps - 1)
            cache[(stone, steps)] = val
            return val

        string = str(stone)
        length = len(string)

        if not length & 1:
            left_val = count(int(string[: length // 2]), steps - 1)
            right_val = count(int(string[length // 2 :]), steps - 1)
            cache[(stone, steps)] = left_val + right_val
            return left_val + right_val

        val = count(stone * 2024, steps - 1)
        cache[(stone, steps)] = val
        return val

    print(sum(count(stone, 75) for stone in pebbles))


def part1(pebbles):
    total = 0
    iter_count = 25
    for peb in pebbles:
        stack = [(peb, 0, 1)]
        peb_count = 0

        while len(stack):
            cur_peb, i, count = stack.pop()

            if i == iter_count:
                peb_count += 1
                continue

            if cur_peb == 0:
                cur_peb = 1
                stack.append((cur_peb, i + 1, count))
                continue

            if not len(str(cur_peb)) & 1:
                p = str(cur_peb)
                mid = len(p) // 2
                left_half = int(p[:mid])
                right_half = int(p[mid:])
                stack.append((left_half, i + 1, count))
                stack.append((right_half, i + 1, count))
                continue

            stack.append((cur_peb * 2024, i + 1, count))

        total += peb_count
    print(total)


def main():
    test = False
    inputs = get_input(test=test)
    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()
