"""
libgol
~~~~~~

This module contains the primary object to run the Game of Life.
"""

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Grid:
    """An object to represent the Game of Life grid.

    Parameters
    ----------
    size_x : int
        Size of grid along x
    size_y : int
        Size of grid along y
    initial : list, optional
        List of (x, y) index pairs defining the grid's initial set of live
        cells. If no argument is given, a random initial state is used.
    """

    def __init__(self, size_x, size_y, initial=None):
        self.size_x = size_x
        self.size_y = size_y
        self.data = np.zeros((size_x, size_y), dtype=bool)

        if initial is None:
            initial = self._gen_random_initial()

        for index in initial:
            self.data[index] = True

    def _gen_random_initial(self):
        """Generate a random initial state."""
        n_cells = self.size_x * self.size_y

        # Random number of live cells
        rng = np.random.default_rng()
        n = rng.integers(round(n_cells * 0.25), n_cells)

        indices = []
        for _ in range(n):
            indices.append(
                (rng.integers(0, self.size_x - 1), rng.integers(0, self.size_y - 1))
            )

        return indices

    def get_neighbour_indices(self, x, y):
        """Returns a list of (x, y) index pairs corresponding to the neighbours of a
        given cell.

        If the neighbour does not exist (i.e. at edge of grid), the index of that
        "neighbour" is set to *None*.
        """
        # fmt: off
        neighbours = [
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),  
            (x - 1, y),                 (x + 1, y),  
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),  
        ]
        # fmt: on

        # Neighbours that do not exist (outside of grid)
        if x == 0:
            neighbours[0] = None
            neighbours[3] = None
            neighbours[5] = None

        if y == 0:
            neighbours[5] = None
            neighbours[6] = None
            neighbours[7] = None

        if x == self.size_x - 1:
            neighbours[2] = None
            neighbours[4] = None
            neighbours[7] = None

        if y == self.size_y - 1:
            neighbours[0] = None
            neighbours[1] = None
            neighbours[2] = None

        return neighbours

    def update(self):
        """Apply the rules of the game and update the grid."""
        next_gen = np.copy(self.data)

        # Loop through every cell
        for i in range(self.size_x):
            for j in range(self.size_y):
                # Count number of live neighbours
                n_live_nbrs = 0
                for nbr in self.get_neighbour_indices(i, j):
                    if nbr is None:
                        continue
                    if self.data[nbr]:
                        n_live_nbrs += 1

                # Apply the rules of the game
                if self.data[(i, j)]:
                    # Rule 1: Any live cell with two or three live neighbours survives
                    if n_live_nbrs in {2, 3}:
                        pass
                    else:
                        next_gen[(i, j)] = False

                elif not self.data[(i, j)] and n_live_nbrs == 3:
                    # Rule 2: Any dead cell with three live neighbours becomes a live cell
                    next_gen[(i, j)] = True

                else:
                    # Rule 3: All other live cells die in the next generation.
                    # Similarly, all other dead cells stay dead.
                    next_gen[(i, j)] = False

        self.data = next_gen

    def draw(self):
        """Draw the grid as ASCII text.

        Print "*" if the cell is alive.
        Print "o" if the cell is dead.
        """
        for i in range(self.size_x):
            for j in range(self.size_y):
                if self.data[(i, j)]:
                    print("*", end="")
                else:
                    print("o", end="")
            print("")
        print("")


class GameOfLife:
    """An object to run the Game."""

    def __init__(self, x, y, initial):
        self.grid = Grid(x, y, initial)

    def run(self, speed):
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid.data)

        def _update_grid(frame_num, img):
            self.grid.update()
            img.set_data(self.grid.data)
            return [img]  # Return as iterable for blitting

        ani = animation.FuncAnimation(
            fig,
            _update_grid,
            fargs=(img,),
            init_func=lambda: [img],
            interval=speed,
            blit=True,
        )

        plt.show()
