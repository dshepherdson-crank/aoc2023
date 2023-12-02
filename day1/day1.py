import re

dict_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1():
    file = open("input.txt", "r")
    total = 0

    for line in file:
        results = re.findall(r"\d+", line)
        print(results[0][0], results[-1][-1])
        total += int(results[0][0] + results[-1][-1])
    print(f"The total for part 1 is {total}")


def part2():
    file = open("input.txt", "r")
    total = 0

    for line in file:
        line.strip()
        all_results = re.findall(
            re.compile(r"(?=(\d+|" + "|".join(dict_map) + "))"), line
        )
        f1 = all_results[0]
        f2 = all_results[-1]
        v1 = (f1 in dict_map) and dict_map[f1] or f1[0]
        v2 = (f2 in dict_map) and dict_map[f2] or f2[-1]
        print(line, all_results, v1 + v2)
        total += int(v1 + v2)

    print(f"The total for part 2 is {total}")


if __name__ == "__main__":
    # part1()
    part2()
