# Conway's Game of Life

My implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using Python and [`matplotlib`](https://matplotlib.org/) for the animation.

## Usage

```console
$ ./game-of-life.py [-x <grid-size-x>] [-y <grid-size-y>] [-i <initial-state>] [-s <animation-speed>]
```

A few initial states are included, which can be specified using the `-i` option:

* `random`: Fill the grid randomly with live and dead cells.
* `rpentomino`: The [R-pentomino](https://en.wikipedia.org/wiki/Pentomino), a well known "methuselah" seed pattern.
* `diehard`: The *Diehard* seed pattern, which disappears after 130 generations.
