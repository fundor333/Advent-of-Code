import unittest

def get_data():
    with open("input/input2.txt", "r") as f:
        data = f.read()
    return [int(x) for x in data.split(",")]


def part1(data, noun=12, verb=2):
    ptr = 0
    program_text = data[:]
    program_text[1] = noun
    program_text[2] = verb
    while ptr<=len(program_text):
        if program_text[ptr] == 1:
            program_text[program_text[ptr + 3]] = program_text[program_text[ptr + 1]] + program_text[program_text[ptr + 2]]
        elif program_text[ptr] == 2:
            program_text[program_text[ptr + 3]] = program_text[program_text[ptr + 1]] * program_text[program_text[ptr + 2]]
        elif program_text[ptr] == 99:
            return program_text[0]
        ptr += 4
    print("SHOULDN'T HAPPEN")


def part2(data):
    for noun in range(100):
        for verb in range(100):
            if part1(data, noun, verb) == 19690720:
                return 100 * noun + verb


if __name__ == "__main__":
    data = get_data()
    print(part1(data))
    print(part2(data))

