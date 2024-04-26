#!/usr/bin/env python3

import argparse
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

parser = argparse.ArgumentParser(description='Tromino tiling visualizer')
parser.add_argument('-o', '--output', type=str, help='Output file')
args = parser.parse_args()  

fig, ax = plt.subplots()

for row, line in enumerate(sys.stdin):
    colors = line.split()
    for column, color in enumerate(colors):
        match color:
            case 'X':
                color = 'k'
            case 'R':
                color = '#e41a1c'
            case 'G':
                color = '#4daf4a'
            case 'B':
                color = '#377eb8'
        rect = Rectangle((column, -row), 1, 1, 
                         edgecolor='k', facecolor=color)
        ax.add_patch(rect)
ax.grid(True)

plt.axis('equal')
plt.axis('off')
if args.output:
    plt.savefig(args.output)
plt.show()
