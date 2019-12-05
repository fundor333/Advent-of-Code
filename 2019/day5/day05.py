import unittest

def read_file(name):
    with open(f"input/{name}") as f:
        content = f.readlines()
    return [x.strip() for x in content]


def split_instruction(instruction):
    instruction = f"{instruction:05}"
    return instruction[3:], instruction[0:3]


def get_values(input, position, program_text, modes):
    mode_a, mode_b, mode_c = modes
    values = []

    if program_text in ["01", "02", "04", "05", "06", "07", "08"]:
        if mode_c == "0":
            values.append(input[input[position + 1]])
        else:
            values.append(input[position + 1])

        if program_text in ["01", "02", "05", "06", "07", "08"]:
            if mode_b == "0":
                values.append(input[input[position + 2]])
            else:
                values.append(input[position + 2])

            if program_text in []:
                if mode_a == "0":
                    values.append(input[input[position + 3]])
                else:
                    values.append(input[position + 3])

    return values


def esercizio1():
    prog = read_file("input.txt")[0].split(",")
    prog = [int(x) for x in prog]

    i = 0
    input = 5

    while prog[i] != 99:
        program_text, modes = split_instruction(prog[i])
        values = get_values(prog, i, program_text, modes)

        if program_text == "01":
            prog[prog[i + 3]] = values[0] + values[1]
            i += 4

        if program_text == "02":
            prog[prog[i + 3]] = values[0] * values[1]
            i += 4

        if program_text == "03":
            prog[prog[i + 1]] = input
            i += 2

        if program_text == "04":
            print(values[0])
            i += 2


def esercizio2():
    prog = read_file("input.txt")[0].split(",")
    prog = [int(x) for x in prog]

    i = 0
    input = 5

    while prog[i] != 99:
        program_text, modes = split_instruction(prog[i])
        values = get_values(prog, i, program_text, modes)

        if program_text == "01":
            prog[prog[i + 3]] = values[0] + values[1]
            i += 4

        if program_text == "02":
            prog[prog[i + 3]] = values[0] * values[1]
            i += 4

        if program_text == "03":
            prog[prog[i + 1]] = input
            i += 2

        if program_text == "04":
            print(values[0])
            i += 2

        if program_text == "05":
            if values[0]:
                i = values[1]
            else:
                i += 3

        if program_text == "06":
            if not values[0]:
                i = values[1]
            else:
                i += 3

        if program_text == "07":
            if values[0] < values[1]:
                prog[prog[i + 3]] = 1
            else:
                prog[prog[i + 3]] = 0
            i += 4

        if program_text == "08":
            if values[0] == values[1]:
                prog[prog[i + 3]] = 1
            else:
                prog[prog[i + 3]] = 0
            i += 4


if __name__ == '__main__':
    esercizio1()
    esercizio2()
