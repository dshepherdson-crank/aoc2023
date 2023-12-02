import re


def get_game_id(str):
    id = re.findall(r"(?<=Game )\d+", str)
    return int(id[0])


def get_set_distribution(set):
    r = re.findall(r"\d+(?= red)", set)
    g = re.findall(r"\d+(?= green)", set)
    b = re.findall(r"\d+(?= blue)", set)

    r = int((len(r) > 0) and r[0] or 0)
    g = int((len(g) > 0) and g[0] or 0)
    b = int((len(b) > 0) and b[0] or 0)

    return r, g, b


def part1(red, green, blue):
    file = open("input.txt", "r")
    total = 0

    for line in file:
        line.strip()
        gamestr, setstr = line.split(":")
        sets = setstr.split(";")
        id = get_game_id(gamestr)
        include = True

        for set in sets:
            r, g, b = get_set_distribution(set)
            if red < r or green < g or blue < b:
                include = False

        total += include and id or 0

    print(f"The total for part 1 is {total}")


def part2():
    file = open("input.txt", "r")
    total = 0

    for line in file:
        line.strip()
        gamestr, setstr = line.split(":")
        sets = setstr.split(";")
        rmin = 0
        gmin = 0
        bmin = 0

        for set in sets:
            r, g, b = get_set_distribution(set)

            rmin = max(rmin, r)
            gmin = max(gmin, g)
            bmin = max(bmin, b)

        power = rmin * gmin * bmin
        total += power

    print(f"The total for part two is {total}")


if __name__ == "__main__":
    part1(12, 13, 14)
    part2()
