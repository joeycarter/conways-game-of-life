#!/usr/bin/env python3

"""
Conway's Game of Life
=====================

Run Conway's Game of Life.

The rules of the Game:

    1. Any live cell with two or three live neighbours survives.
    2. Any dead cell with three live neighbours becomes a live cell.
    3. All other live cells die in the next generation. Similarly, all other
       dead cells stay dead.
"""


import argparse
import sys

import libgol


def _docstring(docstring):
    """Return summary of docstring"""
    return " ".join(docstring.split("\n")[4:5]) if docstring else ""


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description=_docstring(__doc__))
    parser.add_argument("--version", action="version", version="%(prog)s 0.1")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="print verbose messages; multiple -v result in more verbose messages",
    )
    parser.add_argument(
        "-x",
        "--grid-x",
        type=int,
        default=10,
        help="size of grid along x (default: %(default)s)",
    )
    parser.add_argument(
        "-y",
        "--grid-y",
        type=int,
        default=10,
        help="size of grid along y (default: %(default)s)",
    )
    parser.add_argument(
        "-i",
        "--init",
        choices=["random", "rpentomino", "diehard"],
        default="random",
        help="name of initial pattern",
    )
    parser.add_argument(
        "-s",
        "--speed",
        type=int,
        help="animation speed; input as delay between frames in milliseconds",
    )

    args = parser.parse_args()

    return args


def main():
    try:
        args = parse_args()

        initial = None
        if args.init == "random":
            pass
        elif args.init == "rpentomino":
            x = int(args.grid_x / 2)  # Grid centre x
            y = int(args.grid_y / 2)  # Grid centre y
            initial = [
                (x, y + 1),
                (x + 1, y + 1),
                (x - 1, y),
                (x, y),
                (x, y - 1),
            ]
        elif args.init == "diehard":
            x = int(args.grid_x / 2)  # Grid centre x
            y = int(args.grid_y / 2)  # Grid centre y
            initial = [
                (x - 3, y),
                (x - 2, y),
                (x - 2, y - 1),
                (x + 3, y + 1),
                (x + 2, y - 1),
                (x + 3, y - 1),
                (x + 4, y - 1),
            ]

        game_of_life = libgol.GameOfLife(args.grid_x, args.grid_y, initial)
        game_of_life.run(args.speed)

    except KeyboardInterrupt:
        return 1


if __name__ == "__main__":
    sys.exit(main())
