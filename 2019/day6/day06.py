#!/usr/bin/env python3

"""
It must work even if COM is not in the first line.
`input.txt` is like that, so I took the example
and randomized its lines to make the example
similar to the real input.
"""

from typing import Dict, List


def read_lines(fname: str) -> List[str]:
    with open(fname) as f:
        return f.read().strip().splitlines()


def cleaner_counter(k, system, orbits):
    if k in orbits:
        orbit_value = orbits[k]
        reachable = system[k]
        for obj in reachable:
            orbits[obj] = orbit_value + 1
        del system[k]
        return


def find_path(parent_path, src):
    path = []
    planet_iterator = src
    while True:
        value = parent_path[planet_iterator]
        path.append(value)
        if value == "COM":
            return path[::-1]
        planet_iterator = value


def generate_system_orbits(lines):
    system = {}
    orbits = {"COM": 0}
    for line in lines:
        planet, satellite = line.split(")")
        if planet not in system:
            system[planet] = [satellite]
        else:
            system[planet].append(satellite)
    return system, orbits


def generate_parents_paths(lines):
    parent_paths = {}
    for line in lines:
        planet, satellite = line.split(")")
        parent_paths[satellite] = planet
    return parent_paths


if __name__ == "__main__":
    lines = read_lines("input/input.txt")
    system, orbits = generate_system_orbits(lines)
    while len(system) > 0:
        copy_system = system.copy()
        for k in copy_system:
            cleaner_counter(k, system, orbits)

    result = sum(orbits.values())
    print(result)

    parents_paths = generate_parents_paths(lines)
    path_you = find_path(parents_paths, "YOU")
    path_SAN = find_path(parents_paths, "SAN")
    result = len(set(path_you).difference(path_SAN)) + len(
        set(path_SAN).difference(path_you)
    )  # https://www.geeksforgeeks.org/python-set-difference/
    print(result)
