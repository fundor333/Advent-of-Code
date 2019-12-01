def counter_fuel(totale, induviduale):
    totale += ((induviduale) // 3) - 2
    return totale


def counter_fuel_with_fuel(totale, induviduale):
    added = ((induviduale) // 3) - 2
    if added > 0:
        added += counter_fuel_with_fuel(0, added)
    if added < 0:
        return 0
    return totale + added


if __name__ == "__main__":
    tot = 0
    with open("input1.txt") as f:
        lines = f.readlines()
        for line in lines:
            tot = counter_fuel(tot, int(line))

        print("Es 1.1 " + tot)
        tot = 0

        lines = f.readlines()
        for line in lines:
            tot = counter_fuel_with_fuel(tot, int(line))
        print("Es 1.2 " + tot)
