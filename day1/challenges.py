import re

with open("input.txt", "r") as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    total = 0

    for line in puzzle_input.split("\n"):
        digits = re.findall(r"(\d)", line)
        total += int(str(digits[0]) + str(digits[-1]))
        print(total, digits[0], digits[-1])
    return total


def part2(puzzle_input):
    total = 0
    word2_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for line in puzzle_input.split("\n"):
        # find letter words
        words = re.findall(
            "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9", line
        )
        # convert words to numbers
        for i in range(len(words)):
            if words[i] in word2_num:
                words[i] = word2_num[words[i]]
        # convert calculate total
        total += int(str(words[0]) + str(words[-1]))
        print(total, words[0], words[-1])
    return total


print("Part 1:", part1(puzzle_input))
print("Part 2:", part2(puzzle_input))
