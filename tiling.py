#!/usr/bin/env python3

import argparse

NW, NE, SE, SW = 0, 1, 2, 3
COLORS = ["R", "G", "B"]
GAP = "X"

ROTATIONS = {NW: SE, NE: SW, SE: NW, SW: NE}
TILE_CONFIGURATIONS = {
    NW: [(1, 0), (0, 1), (1, 1)],
    NE: [(0, 0), (0, 1), (1, 1)],
    SW: [(0, 0), (1, 0), (1, 1)],
    SE: [(0, 0), (0, 1), (1, 0)],
}


def place_tile(grid, x, y, gap, color):
    for dx, dy in TILE_CONFIGURATIONS[gap]:
        grid[x + dx][y + dy] = color
    return grid


def rotate(pos, gap):
    return gap if pos == gap else ROTATIONS[pos]


def tile(grid, n, x=0, y=0, gap=NW):
    if n == 1:
        grid = place_tile(grid, x, y, gap, COLORS[1])
    elif n == 2:
        if x == 0 and y == 0:
            gap = SE

        grid = place_tile(grid, x + 1, y + 1, gap, COLORS[1])

        grid = place_tile(grid, x, y, rotate(NW, gap), COLORS[2])
        grid = place_tile(grid, x + 2, y, rotate(NE, gap), COLORS[0])
        grid = place_tile(grid, x + 2, y + 2, rotate(SE, gap), COLORS[2])
        grid = place_tile(grid, x, y + 2, rotate(SW, gap), COLORS[0])
    else:
        center = 2 ** (n - 1) - 1
        grid = place_tile(grid, x + center, y + center, gap, COLORS[1])

        grid = tile(grid, n - 1, x, y, rotate(NW, gap))
        grid = tile(grid, n - 1, x + center + 1, y, rotate(NE, gap))
        grid = tile(grid, n - 1, x + center + 1, y + center + 1, rotate(SE, gap))
        grid = tile(grid, n - 1, x, y + center + 1, rotate(SW, gap))

    return grid


parser = argparse.ArgumentParser(description="Tromino tiling generator")
parser.add_argument("n", type=int, help="Size of grid (2^n x 2^n)")
args = parser.parse_args()

size = 2**args.n

grid = [[GAP for _ in range(size)] for _ in range(size)]

grid = tile(grid, args.n, gap=NW)

for i in range(size):
    print(" ".join(grid[i]))
