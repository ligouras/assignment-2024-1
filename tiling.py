#!/usr/bin/env python3

import argparse

NW, NE, SE, SW = 0, 1, 2, 3
COLORS = ["R", "G", "B"]
GAP = "X"


def place_tile(grid, x, y, gap, color):
    if gap == NW:
        grid[x + 1][y] = color
        grid[x][y + 1] = color
        grid[x + 1][y + 1] = color
    elif gap == NE:
        grid[x][y] = color
        grid[x][y + 1] = color
        grid[x + 1][y + 1] = color
    elif gap == SW:
        grid[x][y] = color
        grid[x + 1][y] = color
        grid[x + 1][y + 1] = color
    elif gap == SE:
        grid[x][y] = color
        grid[x][y + 1] = color
        grid[x + 1][y] = color

    return grid


def rotate(pos, gap):
    if pos == gap:
        return gap
    if pos == NW:
        return SE
    elif pos == NE:
        return SW
    elif pos == SE:
        return NW
    elif pos == SW:
        return NE


def tile(grid, n, x=0, y=0, gap=NW):
    if n == 1:
        grid = place_tile(grid, x, y, gap, COLORS[1])
    elif n == 2:
        grid = place_tile(grid, x + 1, y + 1, gap, COLORS[1])

        grid = place_tile(grid, x, y, rotate(NW, gap), COLORS[2])
        grid = place_tile(grid, x + 2, y, rotate(NE, gap), COLORS[0])
        grid = place_tile(grid, x + 2, y + 2, rotate(SE, gap), COLORS[2])
        grid = place_tile(grid, x, y + 2, rotate(SW, gap), COLORS[0])
    else:
        center = 2 ** (n - 1) - 1
        grid = place_tile(grid, center, center, gap, COLORS[1])

    return grid


parser = argparse.ArgumentParser(description="Tromino tiling generator")
parser.add_argument("n", type=int, help="Size of grid (2^n x 2^n)")
args = parser.parse_args()

size = 2**args.n

grid = [[GAP for _ in range(size)] for _ in range(size)]

grid = tile(grid, args.n)

for i in range(size):
    print(" ".join(grid[i]))
