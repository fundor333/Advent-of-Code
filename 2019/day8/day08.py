import math
import collections

WIDTH = 25
HEIGHT = 6
PIXER_PER_LAYER = WIDTH * HEIGHT


def break_layers():

    with open("input/input.txt") as file:
        elf_data = []
        for i in file.read().strip():
            elf_data.append(int(i))

    assert len(elf_data) % PIXER_PER_LAYER == 0
    layers = []
    while elf_data:
        layers.append(elf_data[:PIXER_PER_LAYER])
        del elf_data[:PIXER_PER_LAYER]
    return layers


if __name__ == "__main__":

    layers = break_layers()

    fewest_zeros = min(layers, key=lambda layer: layer.count("0"))
    print(fewest_zeros.count("1") * fewest_zeros.count("2"))

    visible = []
    for i in range(PIXER_PER_LAYER):
        for layer in layers:
            color = layer[i]
            if color < 2:
                visible.append(color)
                break
    image = ""
    x = 0
    for y in range(HEIGHT):
        for pixel in (i for i in visible[x : x + WIDTH]):
            if pixel == 0:
                image += " "
            elif pixel == 1:
                image += "#"
        image += "\n"
        x += WIDTH
    print(image)  # LEGJ
