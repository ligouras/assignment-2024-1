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


def tile(grid, n, x=0, y=0, gap=NW):
    if n == 1:
        grid = place_tile(grid, x, y, gap, COLORS[1])
    if n == 2:
        grid = place_tile(grid, x + 1, y + 1, NW, COLORS[1])

        grid = place_tile(grid, x, y, NW, COLORS[2])
        grid = place_tile(grid, x + 2, y, SW, COLORS[0])
        grid = place_tile(grid, x + 2, y + 2, NW, COLORS[2])
        grid = place_tile(grid, x, y + 2, NE, COLORS[0])

    return grid


parser = argparse.ArgumentParser(description="Tromino tiling generator")
parser.add_argument("n", type=int, help="Size of grid (2^n x 2^n)")
args = parser.parse_args()

n = args.n
size = 2**n

grid = [[GAP for _ in range(size)] for _ in range(size)]

grid = tile(grid, n)

for i in range(size):
    print(" ".join(grid[i]))
