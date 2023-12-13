import re


def part1(input_str, red_count, green_count, blue_count):
    possible_games = []
    # open the file
    with open(input_str, "r") as f:
        input_str = f.read()
    for line in input_str.split("\n"):
        game_id = re.findall(r"Game (\d+):", line)
        print(game_id)
        invalid = False

        # sum of blue
        blue = re.findall(r"(\d+) blue", line)
        for i in range(len(blue)):
            blue[i] = int(blue[i])
            print("bluecalc", blue[i], blue_count)
            if blue[i] > blue_count:
                print("invalid", game_id[0])
                invalid = True
                break
            else:
                print("bvalid", game_id[0])

        green = re.findall(r"(\d+) green", line)
        for i in range(len(green)):
            green[i] = int(green[i])
            print("greencalc", green[i], green_count)
            if green[i] > green_count:
                print("invalid", game_id[0])
                invalid = True
                break
            else:
                print("gvalid", game_id[0])

        red = re.findall(r"(\d+) red", line)
        print(red[0])
        for i in range(len(red)):
            red[i] = int(red[i])
            if red[i] > red_count:
                print("invalid", game_id[0])
                invalid = True
                break
            else:
                print("rvalid", game_id[0])

        # sum of all valid games
        if invalid == False:
            possible_games.append(game_id[0])
            print("valid", game_id[0])

    total = 0
    for i in range(len(possible_games)):
        possible_games[i] = int(possible_games[i])
        total += possible_games[i]
    print(possible_games, total)


red_count = 12
green_count = 13
blue_count = 14

result = part1(
    input_str="input.txt",
    red_count=red_count,
    green_count=green_count,
    blue_count=blue_count,
)


# Minimum set of cubes
def part2(input_str):
    total = []
    # open the file
    with open(input_str, "r") as f:
        input_str = f.read()
    for line in input_str.split("\n"):
        game_id = re.findall(r"Game (\d+):", line)
        print(game_id)

        blue_l = 0
        green_l = 0
        red_l = 0

        # sum of blue
        blue = re.findall(r"(\d+) blue", line)
        for i in range(len(blue)):
            blue[i] = int(blue[i])
            if blue[i] > blue_l:
                blue_l = blue[i]
                print("blue max", blue_l)

        green = re.findall(r"(\d+) green", line)
        for i in range(len(green)):
            green[i] = int(green[i])
            if green[i] > green_l:
                green_l = green[i]
                print("green max", green_l)

        red = re.findall(r"(\d+) red", line)
        for i in range(len(red)):
            red[i] = int(red[i])
            if red[i] > red_l:
                red_l = red[i]
                print("red max", red_l)

        power = blue_l * green_l * red_l
        print("power", power)
        total.append(power)

    print("power of the minimum set of cubes", sum(total))


part2(input_str="input.txt")
